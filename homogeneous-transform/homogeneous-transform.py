import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    T      = np.array(T, dtype=float)
    points = np.array(points, dtype=float)
    single = points.ndim == 1

    if single:
        points = points[np.newaxis, :]           # (1,3)

    ones     = np.ones((len(points), 1))
    ph       = np.hstack([points, ones])         # (N,4)
    ph_prime = (T @ ph.T).T                      # (N,4)

    result = ph_prime[:, :3]                     # drop w

    return result[0] if single else result