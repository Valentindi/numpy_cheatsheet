import numpy as np


# divide matrix by row-sums
mat = np.mat([[4,2],[2,3]])
print(mat/mat.sum(axis=1))

# divide matrix by col-sums
mat = np.mat([[1,2],[3,4]])
print(mat/mat.sum(axis=0))