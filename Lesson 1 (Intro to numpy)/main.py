import numpy as np

arr = np.array([10,20,30,40,50])

print("1d array")
print(arr)

print("dimensions: ",arr.ndim)
print("shape: ",arr.shape)

#2d array
arr = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print("2D array: ")
print(arr)

print("dimensions: ",arr.ndim)
print("shape: ",arr.shape)

#3d Array

arr = np.array(
    [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]

        ],
        
        [
            [9,10],
            [11,12]
        ]
    ]
)

print("3D array: ", arr)
print("dimensions: ", arr.ndim)
print("shape: ", arr.shape)