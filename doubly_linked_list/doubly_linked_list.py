#!/usr/bin/env python
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def get_length_value(self):
        self.length_val = 0
        node = self.head
        while node is not None:
            self.length_val += 1
            node = node.next
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # check if list is empty.
        if self.head is None:
            # create new node
            new_node = ListNode(value)
            
            # add new node to head   
            self.head = new_node
            # add new node to tail
            self.tail = new_node
            # increment length by 1
            self.get_length_value()
        else:
            # * at least one node in list
            # create ListNode in new_node
            new_node = ListNode(value)
            # head now points to ==> next new_node
            new_node.next = self.head
            # new_node now points to ==> prev head
            self.head.prev = new_node
            # new_node now pointing to ==> head
            self.head = new_node
            # increment length by 1
            self.length += 1


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    #! NEED TO DO
    def remove_from_head(self):
        # if head not exists return none
        if self.head is None:
            return None
        # if list == 1
        if self.length == 1:
            head_val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_val
        else:
            head_val = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return head_val
            
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # if list is empty
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node = ListNode(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if head not exists return none
        if self.tail is None:
            return None
        # if list == 1
        if self.length == 1:
            tail_val = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return tail_val
        else:
            tail_val = self.tail.value
            self.tail = self.tail.prev
            # self.tail.next = None
            self.length -= 1
            return tail_val
            
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    #! NEED TO DO
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    
    def move_to_end(self, node):
        # check list empty
        if self.length == 0:
            return None
        # check if 1 item in list
        # return none no where to move
        if self.length == 1:
            return None
        else:
            # save node that will be moving value
            node_val = node.value
            self.delete(node)
            # move the node_val to the end
            self.add_to_tail(node_val)




        #* Temp pointer for the node we are searching for
        #* O(1)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    '''
    check for empty pointers
    get prev node = node.prev
    set prev_node.next to node.next
    next_node = node.next
    set next_node.prev = prev_node
    decrement length
    set node.prev = none
    set node.next = none
    return node.value
    
    '''

    def delete(self, node):
        # if  none return & return length for 0
        if self.length == 0:
            return None
        # if head == tail point both to None
        # decrement length by 1
        # recurse check.
        elif self.length == 1:
            if self.head != node:
                return None
            else:
                self.head = None
                self.tail = None
                self.length -= 1
                return node
        # if removing from head
        elif self.head == node:
            self.remove_from_head()
        # if removing from tail
        elif self.tail == node:
            self.remove_from_tail()
        else: 
            # prev_node
            node.prev.next = node.next

            # prev_node = node.prev

            # next_node = node.next
            # prev_node.next = node.next # next_node

            # # next_node.prev = prev_node #! node.prev doesnt work but prev_node does?! >:Z

            # node.prev = None # pointer disconnect
            # node.next = None # pointer disconnect

            self.length -= 1
            return node
        
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # start max value as the head.value
        current_max = self.head.value
        # set node currently on head
        current_node = self.head
        # iterate through list stop when hits None
        while current_node:
            # compare current_max to current node value update IF value > current_max
            if current_node.value > current_max:
                current_max = current_node.value
        # move node to forward to next node.    
            current_node = current_node.next
        # return max value
        return current_max
    '''
        get max: return max value in list
        if len == 0 return none
        if length == 1 return self.head/tail
        current_max var
        iterate through list
        stop when current_node is None
        compare current_max to each value & update
        current_max if value > current_max
            return current_max
    '''
    