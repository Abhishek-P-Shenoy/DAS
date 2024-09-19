# Creating arrays
import numpy as np

# Creating array using list
userslist = ["abhishek","harshada","Nithin","Ramesh","Nihar"]
user1 = np.array(userslist)

# Creating array using tuple
usertuple = ("abhi","Nihar")
user2 = np.array(usertuple)

# If we need to create a specific type of array we can use the parameter dtype
user3 = np.array([1,2,3,4,5],dtype= int)

# Create array using array library
import array
arr = array.array('i',[1,2,3,4,5]) # here i indicates the type int.

# In order to print the array to terminal we need to run a loop
for user in user2:
    print(user)

# Array using numpy methods
b = geek.zeros(2, dtype = int)

# To create matix or 2D , 3D arrays 
arrayzero1D = np.zeros(2, dtype = int)
arrayzero2D = np.zeros([2,2], dtype=int)

# using range method to create this 
x = np.arange(3, 10, 2) # here x has value [3 5 7 9] here (start, end, interval)

# to view using method
v = user.view() 
print(v.base)

