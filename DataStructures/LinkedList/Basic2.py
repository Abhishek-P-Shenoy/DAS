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
        self.head.next = newNode
    
    def insertInBetween(self,location, data):
        newNode = node(data)
        count = 0
        temp = self.head
        while(temp):
            if(count == location-1):
                newNode.next = temp.next
                temp.next = newNode
                return 
            else:
                count += 1
                temp = temp.next
    def travarse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            while(self.head):
                print(self.head.data,end=" ")
                self.head = self.head.next

        

newSingleLinkedList = sll()
newSingleLinkedList.insertFromTop(1)
newSingleLinkedList.insertFromTop(2)
newSingleLinkedList.insertFromTop(3)
newSingleLinkedList.travarse()