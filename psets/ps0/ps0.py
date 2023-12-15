#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root

class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    if not v:
        return 0 # Base Case: No leaves

    left_size = calculate_sizes(v.left)
    right_size = calculate_sizes(v.right)
    v.size = 1 + left_size + right_size

    return v.size
#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(n)

def find_vertex(r):
    # Your code goes here
    n = r.size
    
    if not r.left and not r.right:
        return r
    def move_to_greatest(v):
        if v:
            if v.parent and r.size - v.size <= n / 2:
                return v
            if v.left and v.left.size <= n / 2:
                return v
            if v.right and v.right.size <= n / 2:
                return v
            
            if v.left and v.right:
                if v.left >= v.right:
                    return move_to_greatest(v.left)
                else:
                    return move_to_greatest(v.right)
            elif v.left and not v.right:
                return move_to_greatest(v.left)
            else:
                return move_to_greatest(v.right) 
        else:
            return None

    return move_to_greatest(r)
'''
def main():
    root = BTvertex(key=0)
    one = BTvertex(key=1)
    two = BTvertex(key=2)
    three = BTvertex(key=3)

    x = BinaryTree(root)
    x.left = one
    x.right = two
    two.right = three
    calculate_sizes(x.root)
    print(find_vertex(x.root).key)

if __name__ == '__main__':
    main()
'''
