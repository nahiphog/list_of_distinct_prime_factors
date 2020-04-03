import numpy as np
from scipy.linalg import solve

A=np.array([[3,4,7], [2,-2,11], [11,-7,15]])
b=np.array([[5,12,7]])
x = solve(A, b.T)
y = np.linalg.det(A)

print(x,y)

#######################

# Importing numpy as np
import numpy as np
 
A = np.array([[6, 1, 1],[4, -2, 5], [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))
