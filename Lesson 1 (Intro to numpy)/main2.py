#create an array of 0's

import numpy as np

arr1 = np.zeros(5)
print(arr1)

#2d zero Array

arr2 = np.zeros((3,4))
print(arr2)

#array of 1's

arr3 = np.ones(5)
print(arr3)

#2d ones array

arr4 = np.ones((3,4))
print(arr4)

#specific data type

arr = np.array([1,2,3,4],dtype = "int")
print(arr)
print(arr.dtype)
#create array using arrange
arr = np.arange(1,11)
print(arr)

#create an array using step size

arr = np.arange(0,20,2)
print(arr)

#reshape array

arr = np.arange(1,10)
newarr = arr.reshape(3,3)
print(newarr)
#sort an array

arr = np.array((8,3,5,6,1,9,2))
sorted_arr = np.sort(arr)
print(sorted_arr)

#sort descending

arr = np.array((8,3,5,6,1,9,2))
desc_array = np.sort(arr)[::-1]
print(desc_array)


#sort 2d array descend

arr = np.array([

    [8,2,5],
    [7,1,9]
])

sorted_arr = np.sort(arr)[:,::-1]
print(sorted_arr)

#accessing an element in 1d array

arr = np.array([10,20,30,40,50])
print("First element is",arr[0])
print("fourth element is",arr[3])

#access in 2d arraw

arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[0,1])
print(arr[1,1])