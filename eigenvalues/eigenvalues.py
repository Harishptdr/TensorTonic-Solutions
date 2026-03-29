import numpy as np

def calculate_eigenvalues(matrix):
    try:
        if matrix is None or len(matrix) == 0:
            return None
        row_len = len(matrix[0])
        if any(not hasattr(r, '__len__') or len(r) != row_len for r in matrix):
            return None
        if len(matrix) != row_len:
            return None
        vals = np.linalg.eigvals(np.array(matrix, dtype=np.complex128))
        vals = np.round(vals, decimals=10)  # fix floating point noise
        return vals[np.lexsort((vals.imag, vals.real))]
    except Exception:
        return None