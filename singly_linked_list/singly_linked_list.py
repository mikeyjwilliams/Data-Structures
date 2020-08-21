

class Node:
    def __init__(self, value, next_node=None):
        # value at this linked list node
        self.value = value
        # reference to next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value

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
            # create a new node with the value we want to add, next_node = None
            new_tail = Node(value, None)
            # set current tail.next_node to the new node
            old_tail = self.tail
            old_tail.next_node = new_tail
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
            #  set self.head to current_head.next_node / None
            current_head = self.head
            self.head = None
            # set tail to None
            self.tail = None
            # decrement
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next_node
            # return current_head.value
            self.length = self.length - 1
            return current_head.value

    # Remove Tail:
    def remove_tail(self):
        # Check if it's there
        if not self.tail:
            return None
        # if self.head is self.tail:
        #     value = self.head
        if self.tail == self.head:
            current_tail = self.tail
            # set tail to None
            self.head = None
            self.tail = None
            return current_tail.value
            # decrement
        
        node = self.head
        while node.next_node != self.tail:
            node = node.next_node
        # once exit while loop current_node pointing to node
        value = self.tail.value
        self.tail = node
        self.length = self.length -1
        return value 


    def add_to_head(self, value):
        # if no head / empty list:
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value, self.head)

    # * add to head
    # is there a head
    # if no head empty
    # a create new node
    # with next = node
    # set head = new node
    # set tail = new node
    # if head:
    # create new node
    # new_node next pointer to head
    # set the head to the new node
    # increment length + 1
    # runtime O(n) => 

    # Remove at index
    # check length > i if not return None
    # --> need a pointer to prev node
    # iterate through loop I times
    # current = head
    # for i times....
    #   current = current.next
    # to_remove = curnode.next
    def remove_at_index(self, index):
        if index >= self.length:
            return None

        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length = self.length -1
            return target.value

        prev_node = self.head
        for i in range(index - 1):
            prev_node = prev_node.next

        target = prev_node.next
        prev_node.next = target.next
        target.next = None

        self.length = self.length - 1
        return target.value