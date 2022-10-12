import numpy as np

matrix = np.array([
    [1, 6, 7],
    [3, 0, 1],
    [8, 1, 9]
])

def solve(matrix):
   Max = np.max(matrix, axis = 0)
   Min = np.min(Max)
   return print(Max), print(Min)


np.vectorize(solve)
solve(matrix)