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