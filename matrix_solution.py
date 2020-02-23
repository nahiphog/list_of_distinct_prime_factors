import numpy as np
from scipy.linalg import solve

A=np.array([[3,4,7], [2,-2,11], [11,-7,15]])
b=np.array([[5,12,7]])
x = solve(A, b.T)

print(x)
