#----- Find Middle of the Linked List

# Create a linked list

class node :
    def __init__(self, x):
        self.data = x
        self.next = None

def getLength(head):
    lenght = 0
    while head:
        lenght += 1
        head = head.next
    return lenght

def getMiddle(head):
    lenght = getLength(head)
    print(lenght)
    mid = lenght/2
    print(mid)
    while (mid):
        head = head.next
        mid -= 1
    return head.data

def insert_form_head(head,data):
    nextNode = node(data)
    nextNode.next = head
    return nextNode

def print_to_list(head):
    while(head is not None):
        print(head.data)
        head = head.next

Node1 = node(1)
Node1 = insert_form_head(Node1 , 2)
Node1 = insert_form_head(Node1 , 5)
Node1 = insert_form_head(Node1 , 2)
Node1 = insert_form_head(Node1 , 2)
print_to_list(Node1)

getMiddle(Node1)
