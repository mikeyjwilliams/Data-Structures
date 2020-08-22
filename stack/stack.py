
import time
from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1
        return self.storage.insert(0, value)


    def pop(self):
        if self.size == 0:
            pass
        else:
            self.size -= 1
            return self.storage.pop()


n = 100000
stack1 = Stack()
start = time.time()
for i in range(n):
    stack1.push(i)
print('push to back ', time.time() - start)

n = 100000
stack2 = Stack()
start = time.time()
for i in range(n):
    stack2.pop()
print('pop to back ', time.time() - start)