import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.sort(np.array(x, dtype=float))
    q = np.array(q, dtype=float)
    n = len(x)

    indices = (q / 100) * (n - 1)
    lower = np.floor(indices).astype(int)
    upper = np.clip(lower + 1, 0, n - 1)
    fraction = indices - lower

    return x[lower] + fraction * (x[upper] - x[lower])