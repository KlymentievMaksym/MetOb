import numpy as np


def ThomasAlgorithm(left_diag: np.ndarray, central_diag: np.ndarray, right_diag: np.ndarray, b: np.ndarray) -> np.ndarray:
    """ Solve Ax = b if A is tridiagonal matrix (with diagonal elements: left_diag, central_diag, right_diag, and 0 in other elements)

    Args:
        left_diag (np.ndarray): Diagonal under main diagonal, shape: (n-1,)
        central_diag (np.ndarray): Main diagonal, shape: (n,)
        right_diag (np.ndarray): Diagonal over main diagonal, shape: (n-1,)
        b (np.ndarray): b vector, shape: (n,)

    Returns:
        np.ndarray: x vector, shape: (n,)
    """
    assert left_diag.shape[0] == central_diag.shape[0] - 1 == right_diag.shape[0] == b.shape[0] - 1, f"left_diag.shape[0] == central_diag.shape[0] - 1 == right_diag.shape[0] == b.shape[0] - 1, received {left_diag.shape[0]} != {central_diag.shape[0] - 1} != {right_diag.shape[0]} != {b.shape[0] - 1}"

    y, p = np.zeros_like(right_diag), np.zeros_like(b)
    x = np.zeros_like(b)

    y[0] = right_diag[0]/central_diag[0]
    p[0] = b[0]/central_diag[0]

    for i in range(1, y.shape[0]):
        y[i] = right_diag[i] / (central_diag[i] - left_diag[i-1] * y[i-1])
        p[i] = (b[i] - left_diag[i-1] * p[i-1]) / (central_diag[i] - left_diag[i-1] * y[i-1])
    p[-1] = (b[-1] - left_diag[-1] * p[-2]) / (central_diag[-1] - left_diag[-1] * y[-1])

    x[-1] = p[-1]

    for i in range(x.shape[0] - 2, -1, -1):
        x[i] = p[i] - y[i] * x[i+1]

    return x


if __name__ == "__main__":
    left_diag = np.array([1, 2, 3, 4])
    central_diag = np.array([1, 2, 3, 4, 5])
    right_diag = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 3, 4, 5])

    print(ThomasAlgorithm(left_diag, central_diag, right_diag, b))
