import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    X   = np.array(X, dtype=float)
    mean = X.mean(axis=0)
    Z    = X - mean                              # center each feature

    std  = Z.std(axis=0, ddof=1)                # sample std per feature
    Z    = Z / std                               # standardize

    corr = (Z.T @ Z) / (len(X) - 1)            # (p, p) correlation matrix

    return corr