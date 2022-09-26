'''
Q1. While traversing a single-circular linked list, which condition establishes that the traversing element/variable has reached the first element?
Ans.The circular singly linked list has no beginning or end. We can randomly assign a head node and
    corresponding to it the previous node as tail node.
    Sometimes for the purpose of insertion of nodes in the circular linked list, it is beneficial to treat the
    list as a single linked list with an external pointer that points to the last node of the list. If we have a
    pointer last pointing to the last node, then last -> next will point to the first node.
    Reason for the last pointer pointing to the last node instead of the first node is because in that case
    we need to traverse the whole list for the insertion of a node at the beginning and end. If instead of
    the start pointer, we take a pointer to the last node, then in both cases there won’t be any need to
    traverse the whole list. So insertion at the beginning or at the end takes constant time, irrespective of
    the length of the list.
    So in this case, the condition that establishes that we have arrived at the first element/node is that
    the node getting pointed by the last pointer is the last node, which points to the first node.
'''
# Python program to demonstrate 
# circular linked list traversal 
  
# Structure for a Node
class Node:
      
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data 
        self.next = None
  
class CircularLinkedList:
      
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
  
    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
          
        ptr1.next = self.head
  
        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next 
            temp.next = ptr1
  
        else:
            ptr1.next = ptr1 # For the first node
  
        self.head = ptr1 
  
    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print (temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break 
  
  
# Driver program to test above function
  
# Initialize list as empty
cllist = CircularLinkedList()
  
# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)
  
print ("Contents of circular Linked List")
cllist.printList()
    
    
'''  
Q2. What are the practical applications of a circular linked list? (Try to find applications in your
respective fields)
Ans2. Following are the applications of circular linked lists:
      1.Circular linked lists are used to implement important data structures such as queues and
        stacks. Queues are particularly useful for things like streaming video and audio like when you
        are watching movies on netflix or videos on youtube.
      2.Alt + Tab shortcut allows users to switch between different opened applications and usually
        traverses in a circular loop where after reaching the last application, the next application is
        the one opened first
      3.Similarly Windows + T allows one to iterate over taskbar icons where also after reaching the
        last icon, the next icon is the first one on the taskbar.
        4.Particularly in Electrical Engineering, an AC voltage fluctuates between -V and +V. This can
        be simulated using a circular linked list if we take discrete voltage values as nodes and
        traverse over them with required speed.
      4.Round Robin scheduling technique in games.
      5.Audio/Video Streaming
      6.Circular Escalators
        
        '''
