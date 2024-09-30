# Implimentaion using list 

stack1 = []

""" To push value in stack """

stack1.append(1)
stack1.append(2)
stack1.append(3)
print(stack1)

""" To Pop value from a stack"""
print(stack1.pop())
print(stack1)

# Implementation using deque from collections library

from collections import deque

stack2 = deque()

stack2.append(1)
stack2.append(2)
stack2.append(3)
stack2.append(4)
print(stack2)

print(stack2.pop())
print(stack2)

# Implementaion using Lifoqueue from queue library import LIFOqueue

from queue import LifoQueue

stack3 = LifoQueue()
stack3.put(1)
stack3.put(2)
stack3.put(3)
stack3.put(4)
# here we cant use print to print the queue so we need to use other methods like size to find out or to pop things and see.
print(stack3.qsize())
