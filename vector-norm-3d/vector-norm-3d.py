import numpy as np

def vector_norm_3d(v):
    v = np.array(v, dtype=float)
    
    # Single vector (1D)
    if v.ndim == 1:
        return np.sqrt(np.sum(v**2))
    
    # Batch of vectors (2D)
    elif v.ndim == 2:
        return np.sqrt(np.sum(v**2, axis=1))
    
    else:
        raise ValueError("Input must be a single vector (3,) or batch (N,3)")


# Test 1: Single 3D vector
v = [3, 4, 0]
print("Single vector norm:", vector_norm_3d(v))        # 5.0

# Test 2: Another single vector
v = [1, 2, 3]
print("Single vector norm:", vector_norm_3d(v))        # 3.7417

# Test 3: Batch of vectors (N, 3)
batch = [    [1, 0, 0],
    [0, 1, 0],
    [3, 4, 0],
    [1, 2, 3]
]
print("Batch norms:", vector_norm_3d(batch))           # [1. 1. 5. 3.7417]
