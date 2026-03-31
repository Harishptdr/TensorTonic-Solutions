import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    mean   = np.mean(x)
    median = np.median(x)
    mode   = float(Counter(x.tolist()).most_common(1)[0][0])

    return mean, median, mode