

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # next node in the list


class LinkedList:
    def __init__(self):
        self.head = None  # points to first node in list
        self.tail = None  # points to tail node in list
        self.length = 0

    def __str__(self):
        pass

    # append / add ==> add_to_tail
    def add_to_tail(self, value):
        # check if theres tail
        # check if no tail (empty list)
        if self.tail is None:
            new_tail = Node(value, None)
            # set head & tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # if there is a tail (general case):
        else:
            # create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # set self.tail to the new node
            self.tail = new_tail
        self.length += 1
    # remove

    def remove_head(self):
        # if not head (empty list)
        if not self.head:
            return None
        # return none

        # list with one element
        if self.head == self.tail:
            #  set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # set tail to None
            self.tail = None
            # decrement
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            # return current_head.value
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        if not self.tail:
            return None
        current_node = self.head
        # self.head = current_head.next

        if current_node.next == None:
            current_node = self.tail

         # Remove Tail:
        # Check if it's there
        # General case:
        # Start at head and iterate to the next-to-last node
        # Stop when current_node.next == self.tail
        # Save the current_tail value
        # Set self.tail to current_node
        # Set current_node.next to None
        #
        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
