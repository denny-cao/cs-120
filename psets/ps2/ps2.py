class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)

        self.size = 1 
        if self.left is not None:
            self.size += self.left.size
        if self.right is not None:
            self.size += self.right.size
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if direction == "R":
            child_node = None
            if child_side == "L":
                child_node = self.left
            else:
                child_node = self.right

            q = child_node
            p = child_node.left
            a = None
            if child_node.left.left != None:
                a = child_node.left.left
            b = None
            if child_node.left.right != None:
                b = child_node.left.right
            c = None
            if child_node.right != None:
                c = child_node.right

            q.size = 1
            if b != None:
                q.size += b.size
            if c != None:
                q.size += c.size

            p.size = 1
            p.size += q.size
            if a != None:
                p.size += a.size
            
            if child_side == "L":
                # Remove edge from self to q and replace with p
                self.left = None
                self.left = p

                # Set p.right to q
                self.left.right = None
                self.left.right = q

                # Set q.left to b
                self.left.right.left = None
                self.left.right.left = b
            
            else:
                # Remove edge from self to q and replace with p
                self.right = None
                self.right = p

                # Set p.right to q
                self.right.right = None
                self.right.right = q

                # Set q.left to b
                self.right.right.left = None
                self.right.right.left = b
        
        if direction == "L":
            child_node = None
            if child_side == "L":
                child_node = self.left
            else:
                child_node = self.right
            
            p = child_node
            q = child_node.right
            a = None
            if child_node.left != None:
                a = child_node.left
            b = None
            if q.left != None:
                b = q.left
            c = None
            if q.right != None:
                c = q.right
            
            # Set sizes
            p.size = 1
            if a != None:
                p.size += a.size
            if b != None:
                p.size += b.size

            q.size = 1
            q.size += p.size
            if c != None:
                q.size += c.size

            if child_side == "L":
                # Remove edge from self to p and set to q
                self.left = None
                self.left = q

                # Set q.left = p
                self.left.left = None
                self.left.left = p

                # Set p.right = b
                self.left.left.right = None
                self.left.left.right = b
            else:
                # Remove edge from self to p and set to q
                self.right = None
                self.right = q

                # Set q.left = p
                self.right.left = None
                self.right.left = p

                # Set p.right = b 
                self.right.left.right = None
                self.right.left.right = b

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self