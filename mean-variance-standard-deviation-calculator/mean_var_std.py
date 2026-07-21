import numpy as np


def calculate(lst):
    """
    Calculate mean, variance, standard deviation,
    max, min, and sum for a 3x3 matrix.

    Parameters
    ----------
    lst : list
        A list containing exactly 9 numbers.

    Returns
    -------
    dict
        Dictionary containing statistics for
        columns, rows, and the flattened matrix.
    """

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lst).reshape(3, 3)

    calculations = {
        "mean": [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item(),
        ],
        "variance": [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item(),
        ],
        "standard deviation": [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item(),
        ],
        "max": [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item(),
        ],
        "min": [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item(),
        ],
        "sum": [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item(),
        ],
    }

    return calculations
