import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v, dtype=float)
    single = v.ndim == 1
    if single:
        v = v[np.newaxis, :]

    result = np.zeros_like(v)
    for i, vec in enumerate(v):
        norm = np.linalg.norm(vec)
        if norm > 0:
            result[i] = vec / norm

    return result[0] if single else result