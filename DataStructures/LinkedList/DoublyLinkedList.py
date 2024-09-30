# Node for dubly linked list

class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


# The class for doubly linked list

class dll:
    def __init__(self):
        self.head = None
    
    # Insertion operation
    def insertFromTop(self,data):
        newNode = node(data)
        temp = self.head
        if self.head is not None:
            temp.prev = newNode
            newNode.next = self.head
            self.head = newNode

        else:
            self.head = newNode
    # Travers the linked list

        # from top to bottom
    def traversFromTop(self):
        temp = self.head
        while temp.next is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print(temp.data,end=" ")
        # from bottom to top
    def traversFromBottom(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        while temp.prev is not None:
            print(temp.data,end="")
            temp = temp.prev

DoublyLinkedList = dll()
DoublyLinkedList.insertFromTop(1)
DoublyLinkedList.insertFromTop(2)
DoublyLinkedList.insertFromTop(3)
DoublyLinkedList.traversFromTop()

