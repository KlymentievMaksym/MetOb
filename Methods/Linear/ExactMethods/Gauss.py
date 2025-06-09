import numpy as np


def Gauss(A, b):
    """
    Gauss elimination method for solving system of linear equations.

    Parameters
    ----------
    A : 2-d array
        Matrix of coefficients of the system.
    b : 1-d array
        Right-hand side vector.

    Returns
    -------
    x : 1-d array
        Solution vector.
    """
    A_ = A.copy()
    b_ = b.copy()
    x = np.zeros_like(b)
    # Forward elimination
    for col in range(1, A.shape[1]):
        for row in range(col, A.shape[0]):
            # Calculate the multiplier
            zeroiator = (- A_[row, col-1]/A_[col-1, col-1])
            # Add row to the row below multiplied by the multiplier
            A_[row] = A_[row] + A_[col-1] * zeroiator
            # Add the same to the right-hand side
            b_[row] = b_[row] + b_[col-1] * zeroiator

    # Back substitution
    for col in range(A.shape[1]-1, -1, -1):
        result = 0
        for row in range(A.shape[0]-1, col, -1):
            # Calculate the sum of the products of the coefficients and
            # the solutions of the previous rows
            result += A_[col, row] * x[row]
        # Calculate the solution of the current row
        x[col] = (b_[col] - result)/A_[col, col]

    return x


if __name__ == "__main__":
    A = np.array([
        [6.59, 1.28, 0.79, 1.195, -0.21],
        [0.92, 3.83, 1.3, -1.63, 1.02],
        [1.15, -2.46, 5.77, 2.1, 1.483],
        [1.285, 0.16, 2.1, 5.77, -18],
        [0.69, -1.68, -1.217, 9, -6]
    ])
    b = np.array([
        [2.1],
        [0.36],
        [3.89],
        [11.04],
        [-0.27]
    ])
    x = Gauss(A, b)
    print(A @ x)
    print(b)
