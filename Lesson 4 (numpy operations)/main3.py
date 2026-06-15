import numpy as np

#solving an expression

def solve(x):
    return 2 * x+3
x = np.array([1,2,3,4,5])
y = solve(x)
print(y)

#summary
arr = np.array([1,2,3,4,5])
print("Original Array", arr)
print("Slice: ", arr[1:4])
print('Even numbers: ', arr[arr % 2 == 0])
print("Add 10: ",arr+10)
print("Multiply by 2: ",arr*2)

def square(x):
    return x**2

print("Squared values: ",square(arr))