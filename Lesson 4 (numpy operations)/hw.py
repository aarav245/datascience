import numpy as np
x = np.array([[85,88,91],[91,93,76],[92,91,95]])

def solve(x):
    return 3*x^2 + 5*x - 7

grades = solve(x)
print(grades)