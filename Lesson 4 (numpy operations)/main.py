#Basic arithmetic functions on an array
import numpy as np

arr = np.array([10,20,30])

print("Original:",arr)
print("Addition:", arr+5)
print("Subtraction:", arr-5)
print("Multiplication:", arr*5)
print("Division:", arr/2)

#Matrix 2d addtion

mata = np.array([[1,2],[3,4]])

matb = np.array([[5,6],[7,8]])

print(mata+matb)
print(mata-matb)
print(mata*matb)
print(mata/matb)

#Matrix multiplaction but with @
mata = np.array([[1,2],[3,4]])

matb = np.array([[5,6],[7,8]])

print(mata @ matb)

#Matrix multiplaction but with np.dot
mata = np.array([[1,2],[3,4]])

matb = np.array([[5,6],[7,8]])

print(np.dot(mata,matb))
