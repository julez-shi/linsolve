"""Routines for solving a linear system of equations."""
import numpy as np


def gaussian_eliminate(aa, bb):
    """Solves a linear system of equations (Ax = b) by Gauss-elimination

    Args:
        aa: Matrix with the coefficients. Shape: (n, n).
        bb: Right hand side of the equation. Shape: (n,)

    Returns:
        Vector xx with the solution of the linear equation or None
        if the equations are linearly dependent.
    """

    """Solving Matrix"""
    nn = aa.shape[0]
    for j in range(0, nn):
        for i in range(j+1, nn):
            if aa[i, j] == 0:
                continue
            bb[i] = aa[j, j] / aa[i, j] * bb[i] - bb[j]
            aa[i] = aa[j, j] / aa[i, j] * aa[i] - aa[j]

    """Solution-Vector"""
    xx = np.zeros((nn,), dtype=float)
    for k in reversed(range(0, nn)):
        for g in reversed(range(k+1, nn)):
            bb[k] = bb[k] - aa[k, g] * xx[g]
        if aa[k, k] == 0:
            continue
        xx[k] = bb[k] / aa[k, k]
    return xx


aa = np.array([[2.0, 4.0, 4.0], [5.0, 4.0, 2.0], [1.0, 2.0, -1.0]])
dd = np.array([[2.0, 4.0, 4.0], [1.0, 2.0, -1.0], [5.0, 4.0, 2.0]])
bb = np.array([1.0, 4.0, 2.0])

xx, cc = gaussian_eliminate(aa, bb)
xx, ee = gaussian_eliminate(dd, bb)

print(aa)
print(ee)
print(bb)
print(xx)
