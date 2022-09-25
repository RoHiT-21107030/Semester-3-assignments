# Represent a node of doubly linked list
class Family_members:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.previous = None
        self.next = None


class DoublyLinkedList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

        # addNode() will add a node to the list

    def addMember(self, name, age):
        # Create a new node
        newMember = Family_members(name, age)

        # If list is empty
        if (self.head == None):
            # Both head and tail will point to newNode
            self.head = self.tail = newMember
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newMember
            # newNode's previous will point to tail
            newMember.previous = self.tail
            # newNode will become new tail
            self.tail = newMember
            # As it is last node, tail's next will point to None
            self.tail.next = None

            # display() will print out the nodes of the list

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.name, current.age),
            current = current.next


dList = DoublyLinkedList()
# Add nodes to the list
dList.addMember('Name1', 1)
dList.addMember('Name2', 2)
dList.addMember('Name3', 3)
dList.addMember('Name4', 4)
dList.addMember('Name5', 5)

# Displays the nodes present in the list
dList.display()

'''
Q.Try to find a way to link the family members' doubly-linked list based on their relationship.
Ans.One way to link the family members doubly-linked list is by sorting the doubly linked list according to age in decending order.By doing so we will get a doubly linked list in which older generation people will be close to head in double linked list and new generation people will be close to tail in doubly linked list.
'''
