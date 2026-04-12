def expected_calibration_error(y_true, y_pred, n_bins):
    import numpy as np
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    n = len(y_true)

    bin_indices = np.minimum(np.floor(y_pred * n_bins).astype(int), n_bins - 1)

    ece = 0.0
    for b in range(n_bins):
        mask = bin_indices == b
        if mask.sum() == 0:
            continue
        acc = y_true[mask].mean()
        conf = y_pred[mask].mean()
        ece += (mask.sum() / n) * abs(acc - conf)

    return float(ece)