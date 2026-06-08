#Array slicing
import numpy as np

linear_array = np.array([1,2,3,4,5,6,7])

slice_array = linear_array[0:4]
print("Original array:", linear_array)
print("Sliced array:", slice_array)
print("-"*40)
#change the value of the sliced array
arr = np.array([1,2,3,4,5])
sliced_arr = arr[0:4]
sliced_arr[3] = 45
print("Original array: ", arr)
print("Sliced array: ", sliced_arr)
print("-"*40)
#2d array slicing
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
result = arr[0:2, 1:3]
print(result)
print("-"*40)
#3d array slicing
arr = np.array([
    [[1,2,3],
     [4,5,6],
     [7,8,9]],
     
     [[10,11,12],
      [13,14,15],
      [16,17,18]]
])
result = arr[0, 0:2, 0:2]
result2 = arr[1, 0:2, 0:2]
print("Original array:\n", arr)
print("-"*40)
print("Sliced array 1:\n", result)
print("Sliced array 2:\n", result2)