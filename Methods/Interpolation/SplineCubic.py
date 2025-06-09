import numpy as np


def cubic_spline(x: np.ndarray, y: np.ndarray, x_eval: np.ndarray) -> np.ndarray:
    """Computes the cubic spline interpolation for given x and y data points.

    Args:
        x (np.ndarray): Array of x coordinates of the data points.
        y (np.ndarray): Array of y coordinates of the data points.
        x_eval (np.ndarray): Array of x values where the spline is evaluated.

    Returns:
        np.ndarray: Array of interpolated y values corresponding to x_eval.
    """
    n = len(x)
    h = np.diff(x)  # Calculate intervals between x values

    # Set up the tridiagonal matrix A
    A = np.zeros((n, n))
    A[0, 0] = 1
    A[-1, -1] = 1
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]

    # Set up the right-hand side vector b
    b = np.zeros(n)
    for i in range(1, n - 1):
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    # Solve for c coefficients
    c = np.linalg.solve(A, b)

    # Calculate a, b, and d coefficients
    a = y[:-1]
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)
    for i in range(n - 1):
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    # Evaluate the spline at each x_eval
    spline_vals = np.zeros_like(x_eval, dtype=float)
    for idx, xi in enumerate(x_eval):
        i = np.searchsorted(x, xi) - 1
        i = max(min(i, n - 2), 0)  # Clamp i to valid range
        dx = xi - x[i]
        spline_vals[idx] = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3

    return spline_vals


if __name__ == "__main__":
    def func(x):
        return 1 / np.sin(x)**2 - 1
    n = 10
    x = np.linspace(np.pi/6, np.pi/2, n)
    y = func(x)
    x_dense = np.linspace(np.pi/6, np.pi/2, int(1e4))
    x_dense = x_dense[~np.isin(x_dense, x)]
    print(cubic_spline(x, y, x_dense))
