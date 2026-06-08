#creating 15x15 array
import numpy as np
matrix = np.arange(1,226).reshape(15,15)
print(matrix)
print("-"*40)

#extract 5x5 middle portion

slicematrix = matrix[6:11,6:11]
print("Middle 5x5 is: ", slicematrix)
print("-"*40)

#first row

firstrow = matrix[0:1,0:15]
print("first row is: ", firstrow)
print("-"*40)

#last column 

lastcol = matrix[:,-1]
print("Last column is: ", lastcol)
print("-"*40)

#even numbers

evenum = matrix[matrix % 2 == 0]
print("All even numbers are: ", evenum)
print("-"*40)
