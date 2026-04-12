import numpy as np

def chi2_independence(C):
    C = np.array(C, dtype=float)
    
    row_sums = C.sum(axis=1, keepdims=True)
    col_sums = C.sum(axis=0, keepdims=True)
    total = C.sum()
    
    expected = (row_sums * col_sums) / total
    chi_square = np.sum((C - expected) ** 2 / expected)
    
    return round(float(chi_square), 10), expected