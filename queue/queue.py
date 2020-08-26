import sys
sys.path.insert(1, '../singly_linked_list')
from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)


    def dequeue(self):
        if self.size == 0:
            # print(self.size, ' none should be here')
            return None
        # if self.size == 1:

        #     self.storage.remove_tail()
        else:
            self.size -= 1
            self.storage.remove_tail()

q = Queue()
q.enqueue(100)
print('100 && 1 == ', q.size)
q.enqueue(101)
print('101 && 2 == ', q.size)
q.enqueue(105)
print('105 && 3 == ', q.size)
q.dequeue()
print('- 100 && 2 == ', q.size)
q.dequeue()
print('1 == ', q.size)
q.dequeue()
print('0 == ', q.size)
q.dequeue()

