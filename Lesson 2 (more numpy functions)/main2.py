#Reshape Challenge 
#Objective: Understand reshaping rules and valid dimensions.
#Task:
#Create a linear array of 24 elements.


#Reshape it into all possible valid 2D shapes.


##Hint:
#Possible pairs → (1,24), (2,12), (3,8), (4,6), (6,4), (8,3), (12,2), (24,1)

import numpy as np

arr = np.arange(1,25)
print("og array",arr)
print("Original shape",arr.shape)
print("\n"+"="*50)

shapes = [
    (1,24),
    (2,12),
    (3,8),
    (4,6),
    (6,4),
    (8,3),
    (12,2),
    (24,1)
]

for shape in shapes:
    resarr = arr.reshape(shape)
    print("\nReshapes to:",shape)
    print(resarr)
    print("Shape: ",resarr.shape)
    print("-" * 50)