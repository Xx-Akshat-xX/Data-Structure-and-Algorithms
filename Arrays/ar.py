# Basic Array operation - 1) Adding/Changing 2) Concatenating 3) Removing 4) Slicing 5) Looping
from array import *

val = array('i', [1, 2, 3, 4, 5, 2])

# Find Length
print(f'Length of the array: {len(val)}')

# Return the index number of the first instance of the value 2
print(val.index(2))

# 1) Change the value 
val[1] = 3
print(val)

# 2) Concatenating
a = array("i", [1, 5, 2, 6, 2, 9])
b = array("i", [56, 45, 56, 75])
c = a + b
print(c)

# 3) Deleting an item from the array
del val[0]
print(val)

# 3.2) You can also use the pop() method, and specify the position of the element to be removed:
val.pop(3)
print(val)

# 4) Slicing
print(val[0:4])

# 5) Loop though elements of index
for i in val:  # All Values
    print(i)
for j in val[2:4]:  # Specific Values
    print(j)
