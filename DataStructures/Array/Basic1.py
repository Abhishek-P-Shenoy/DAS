#----- Find Middle of the Linked List

# Create a linked list

class Node :
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
    mid = lenght/2
    while (mid):
        head = head.next
        mid -= 1
    return head.data

def main():
    n = node(10)
