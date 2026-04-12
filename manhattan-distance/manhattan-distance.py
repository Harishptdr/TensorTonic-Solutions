import numpy as np

def manhattan_distance(x, y):
    return float(np.sum(np.abs(np.array(x) - np.array(y))))