# Creating arrays
import numpy as np
# Creating array using list
userslist = ["abhishek","harshada","Nithin","Ramesh","Nihar"]
user1 = np.array(userslist)
# Creating array using tuple
usertuple = ("abhi","Nihar")
user2 = np.array(usertuple)
# In order to print the array to console we need to run a loop
for user in user2:
    print(user) 