class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_form_head(head,data):
    nextNode = node(data)
    nextNode.next = head
    return nextNode

def insert_form_tail(head,data):
    nextNode = node(data)
    head.next = nextNode
    return head

def print_to_list(head):
    while(head is not None):
        print(head.data)
        head = head.next


# TO impliment a singlely linked list we need to define a class of sll

class sll:
    # This is to initialize the sll
    def __init__(self):
        self.head = None
    
    def insertFromTop(self,data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode

    def insertFromEnd(self,data):
        newNode = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
    
    def insertInBetween(self,location, data):
        newNode = node(data)
        temp = self.head
        for i in range(1,location-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    def travarse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data,end=" ")
                temp = temp.next
    
    def deleteFromTop(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

        

newSingleLinkedList = sll()
newSingleLinkedList.insertFromTop(1)
newSingleLinkedList.insertFromTop(2)
newSingleLinkedList.insertFromTop(4)
newSingleLinkedList.insertFromEnd(5)
newSingleLinkedList.travarse()
print()
newSingleLinkedList.insertFromEnd(5)
newSingleLinkedList.travarse()
print()
newSingleLinkedList.insertInBetween(1,10)
newSingleLinkedList.travarse()
print()
newSingleLinkedList.deleteFromTop()
newSingleLinkedList.travarse()

