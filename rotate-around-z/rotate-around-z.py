import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    points = np.array(points, dtype=float)
    single = points.ndim == 1
    if single:
        points = points[np.newaxis, :]

    cos_t, sin_t = np.cos(theta), np.sin(theta)

    Rz = np.array([
        [ cos_t, -sin_t, 0],
        [ sin_t,  cos_t, 0],
        [     0,      0, 1]
    ])

    rotated = points @ Rz.T

    return rotated[0] if single else rotated