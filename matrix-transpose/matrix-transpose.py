import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    transpose_of_a = np.transpose(A)
    print("Original Matrix:")
    print(A)
    print("\nTranspose of Matrix:")
    print(transpose_of_a)
    return transpose_of_a