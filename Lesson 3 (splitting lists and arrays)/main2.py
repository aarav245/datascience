#Creating a 7x7 matrix
import numpy as np
matrix = np.arange(1,50).reshape(7,7)
print(matrix)
print("-"*40)

#slicing - extracting 3x3

slicing = matrix[2:5,2:5]

print(slicing)
print("-"*40)

#conditional selection

k = np.array([1,2,3,4,5,6,7,8])
evenum = k[k%2==0]
print(evenum)
print("-"*40)

#conditional selection (Greater than)

arr = np.array([10,25,50,75,100])
great = arr[arr > 50]
print(great)
print("-"*40)

#Incrementing
arr = np.array([1,2,3,4,5])
arr = arr+1
print(arr)