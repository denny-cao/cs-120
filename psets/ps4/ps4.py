import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import math
import random

random.seed(120)

#
# Make Sure to Read the README
#


####################
#                  #
# Your Code Here   #
#                  #
####################


'''
A Las Vegas Algorithm to find a key-value pair (Ij, Kj) such that Kj is an i’th smallest key.
arr: a list of key-value pair tuples
    e.g. [(K0, V0), (K1, V1), ..., (Ki, Vi), ..., (Kn, Vn)] 
    ... in this problem set, the values are irrelevant
i: an integer [0, n-1] 
returns: An key-value pair (Kj, Vj) such that Kj is an i’th smallest key.
'''

def QuickSelect(arr, i):
    if len(arr) == 1:
        return arr[0]
    # Your code here

    # Feel free to use get_random_index(arr) or get_random_int(start_inclusive, end_inclusive)
    # ... see the helper functions below
    p = get_random_index(arr)

    pivot = arr[p]

    arr_less, arr_greater, arr_eq = [], [], []
    for key in arr:
        if key[0] < pivot[0]:
            arr_less.append(key)
        elif key[0] > pivot[0]:
            arr_greater.append(key)
        else:
            arr_eq.append(key)

    n_less, n_eq = len(arr_less), len(arr_eq)

    if i < n_less:
        return QuickSelect(arr_less, i)
    elif i >= n_less + n_eq:
        return QuickSelect(arr_greater, i - n_less - n_eq)
    else:
        return arr_eq[0]

def MedianOf3QuickSelect(arr, i):
    if len(arr) == 1:
        return arr[0]

    # Median-of-three pivot selection
    a = arr[get_random_index(arr)]
    b = arr[get_random_index(arr)]
    c = arr[get_random_index(arr)]

    if a[0] < b[0]:
        if b[0] < c[0]:
            median_of_three = b
        elif a[0] < c[0]:
            median_of_three = c
        else:
            median_of_three = a
    else:
        if a[0] < c[0]:
            median_of_three = a
        elif b[0] < c[0]:
            median_of_three = c
        else:
            median_of_three = b

    pivot = median_of_three

    arr_less, arr_greater, arr_eq = [], [], []
    for key in arr:
        if key < pivot:
            arr_less.append(key)
        elif key > pivot:
            arr_greater.append(key)
        else:
            arr_eq.append(key)

    n_less, n_eq = len(arr_less), len(arr_eq)

    if i < n_less:
        return MedianOf3QuickSelect(arr_less, i)
    elif i >= n_less + n_eq:
        return MedianOf3QuickSelect(arr_greater, i - n_less - n_eq)
    else:
        return arr_eq[0]
'''
Uses MergeSort to resolve a number of queries where each query is to find an key-value pair (Kj, Vj) such that Kj is an i’th smallest key.
arr: a list of key-value pair tuples
    e.g. [(K0, V0), (K1, V1), ..., (Ki, Vi), ..., (Kn, Vn)] 
    ... in this problem set, the values are irrelevant
query_list (aka i_arr): a list of integers [0, n-1] 
returns: An list of key-value pairs such that for each query qi, the i'th element in the returned list is (Kj, Vj) such that Kj is an i’th smallest key.
NOTE: This is different from the QuickSelect definition. This function takes in a set of queries and returns a list corresponding to their results. 
    ... this is to properly benchmark for the experiments. We only want to run MergeSort once and then use that one result to resolve all queries.
'''


def MergeSortSelect(arr, query_list):
    # Only call MergeSort once
    # ... MergeSort has already been implemented for you (see below)
    pass
    sort = MergeSort(arr)
    output = []    
    for query in query_list:
        output.append(sort[query])
    return output


##################################
#                                #
# Experiments: Mostly Complete   #
#                                #
##################################


def experiments():
    # Edit this parameter
    k = [i for i in range(10, 20)]

    # Feel free to edit these initial parameters

    RUNS = 150  # Number of runs for each trial; more runs means better distributions approximation but longer experiment
    HEIGHT = 1.5  # Height of a chart
    WIDTH = 3   # Width of a chart
    # Determines if subcharts share the same axis scale/limits
    # ... since the trails cover a wide range, sharing the same scale/limits can cause some lines to be too small.
    SAME_AXIS_SCALE = False

    # You do not need to edit anything below this line
    # ... however, you are free to investigate how it works

    # The search space for our parameters
    # DO NOT EDIT these parameters for your final figure
    n = [2 ** i for i in range(10, 16)]
    # Our deterministically generated dataset
    fixed_dataset = sorted([(0, K) for K in range(max(n))], key=lambda T: T[1], reverse=True)

    # Records we will use to create the Pandas DataFrame
    n_record = []
    k_record = []
    algorithm_record = []
    ms_record = []
    iter = 0
    for ni in n:
        dataset_size_n = fixed_dataset[:ni]
        for ki in k:
            # Generate the queries according to the problem set instructions specification
            queries = [round(j * ni / ki) for j in range(ki)]

            # QuickSelect Runs
            for _ in range(RUNS):
                # Record Time Taken to Solve All Queries
                start_time = time.time()
                for q in queries:
                    # Copy dataset just to be safe
                    QuickSelect(dataset_size_n.copy(), q)
                seconds = time.time() - start_time
                # Record this trial run
                n_record.append(ni)
                k_record.append(ki)
                ms_record.append(seconds * 1000)  # Convert seconds to milliseconds
                algorithm_record.append("QuickSelect")
            
            # MedianOf3QuickSelect Runs
            for _ in range(RUNS):
                # Record Time Taken to Solve All Queries
                start_time = time.time()
                for q in queries:
                    # Copy dataset just to be safe
                    MedianOf3QuickSelect(dataset_size_n.copy(), q)
                seconds = time.time() - start_time
                # Record this trial run
                n_record.append(ni)
                k_record.append(ki)
                ms_record.append(seconds * 1000)  # Convert seconds to milliseconds
                algorithm_record.append("MedianOf3QuickSelect")

            # MergeSort Runs
            for _ in range(RUNS):
                # Record Time Taken to Solve All Queries
                start_time = time.time()
                # Copy dataset just to be safe
                MergeSortSelect(dataset_size_n.copy(), queries)
                seconds = time.time() - start_time
                # Record this trial run
                n_record.append(ni)
                k_record.append(ki)
                ms_record.append(seconds * 1000)  # Convert seconds to milliseconds
                algorithm_record.append("MergeSort")

            # Print progress
            iter += 1
            print("{} of {} Trials Completed".format(iter, len(n) * len(k)))

    # Create Pandas DataFrame
    data_field_title = "Runtime for {} Runs (ms)".format(RUNS)
    df = pd.DataFrame({
        "N": n_record,
        "K": k_record,
        data_field_title: ms_record,
        "Algorithm": algorithm_record
    })
    plot(df, HEIGHT, WIDTH, SAME_AXIS_SCALE, data_field_title)


def plot(df, height, width, SAME_AXIS_SCALE, data_field_title):
    # Plot with Seaborn
    # ... Establish Rows by N
    # ... Establish Columns by K
    # ... Establish Lines by Algorithm
    g = sns.FacetGrid(df, row="N", col="K", hue="Algorithm", height=height, aspect=width / height,
                      sharex=SAME_AXIS_SCALE, sharey=SAME_AXIS_SCALE)
    # Plot the runtime value
    g.map(sns.kdeplot, data_field_title)
    g.add_legend()
    plt.show()


####################
#                  #
# Helper Functions #
#                  #
####################

def run():
    experiments()


# Feel free to use these function or code your own (as long as it is random)

# A small helper function to return a random integer
def get_random_int(start_inclusive, end_inclusive):
    # Uses the python random randomint function
    # ... this function takes in a start and end - both are inclusive [start,end]
    return random.randint(start_inclusive, end_inclusive)


# A small helper function to return a random integer
def get_random_index(arr):
    # retuns a number from 0 to len-1 for valid indices
    return get_random_int(0, len(arr) - 1)


#########################
#                       #
# Provided (Don't Edit) #
#                       #
#########################

#
# You Do NOT Need to Modify Anything Below This Line
#

def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr


'''
A deterministic sorting algorithm
arr: a list of Key-Value pair tuples
    e.g. [(K0, V0), (K1, V1), ..., (Ki, Vi), ..., (Kn, Vn)] 
returns: a sorted list, sorted according to keys
'''


def MergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr) / 2))

    half1 = MergeSort(arr[0:midpt])
    half2 = MergeSort(arr[midpt:])

    return merge(half1, half2)


if __name__ == "__main__":
    run()
