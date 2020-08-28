"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack import Stack
from queue import Queue



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    '''
    - compare target value to node.value
    if value > node.value:
    
        go right
        if node.right is None:
            create the new node there
        else:
            do the same thing
            insert value into node.right
    else if value < node.value
        go left
        if node.left is None:
            create node
        else:
            do the same thing
            insert value
    '''
    # Insert the given value into the tree

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                new_node = BSTNode(value)
                self.right = new_node
            else:
                self.right.insert(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    # single element returns crom contains.
        # compare target value to node.value
        if self.value == target:
            return target
        # if target > node.value:
        if target > self.value:
            # go right
            # if node.right is None:
            if self.right is None:
            # traverse tree not found
                return False
            # return False
            else:
            # repeat
                return self.right.contains(target)
            # check node.right.contains(target)
        # else if target < node.value
        elif target < self.value:
            # go left
            # if node.left is none:
            if self.left is None:
                return False
            else:
                # else:
                # return node.left.contains(target)
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        # start at root
        if self.right is None:
            # already at most right node
            return self.value
        else:
            # keep going right until cant anymore
            # return that value
            return self.right.get_max()

        # iterate get_max()
        # cur_node = self
        # while cur_node.right is not None:
        #     cur_node = cur_node.right

        # # return 'base case'
        # return cur_node.value

    # Call the function `fn` on the value of each node
    # linear O(n)

    def for_each(self, fn):
        # start at root
        # go left check
        # base case...call back
        fn(self.value)
        # check left
        if self.left is not None:
            # go left
            self.left.for_each(fn)
        # check right
        if self.right is not None:
            # go right
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # check left
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node) 
            


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue() # FIFO means we 
        curr = node
        while curr:
            print(curr.value)               
            if curr.right:                                       
                queue.enqueue(curr.right)
            if curr.left:                                        
                queue.enqueue(curr.left)
            curr = queue.dequeue()

# curr node print value
# if left: push left
# if right push right


# Queue
# left      
# right        

# pop left

# curr left print left

# Queue
# right
# left
# right 

# pop right

# Queue
# left
# right
# left 
# right


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        
        stack = Stack()
        curr = node
        while curr:
            print(curr.value)               
            if curr.right:                                       
                stack.push(curr.right)
            if curr.left:                                        
                stack.push(curr.left)
            curr = stack.pop()

# first pass
# Stack FIFO

# left
# right

# pops left

# second pass pushes on right then left
# Stack FIFO
# left
# right
# right

# third pass pushes on right then left
# Stack FIFO
# left
# right
# right

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print(bst)
# # print("post order")
# # bst.post_order_dft()
