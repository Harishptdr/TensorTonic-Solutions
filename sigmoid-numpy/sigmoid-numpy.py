import numpy as np

def sigmoid(x):
    x = np.array(x, dtype=float)
    return 1 / (1 + np.exp(-x))

# 1D array
x = np.array([-3, -1, 0, 1, 3])
print("1D Output:", sigmoid(x))

# 2D array
x_2d = np.array([[1, 2], [3, 4]])
print("2D Output:\n", sigmoid(x_2d))

# Single value
print("Single value:", sigmoid(2))