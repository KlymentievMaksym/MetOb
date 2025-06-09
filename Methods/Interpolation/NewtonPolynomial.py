import numpy as np


def f(Xs_indexes: np.ndarray, Xs_values: np.ndarray, ys_values: np.ndarray) -> float:
    """Recursive computation of divided differences.

    Args:
        Xs_indexes (np.ndarray): Array of indexes
        Xs_values (np.ndarray): Array of x values
        ys_values (np.ndarray): Array of y values

    Returns:
        float: Computed value of divided differences
    """
    assert len(Xs_indexes) > 1, "len(Xs_indexes) must be > 1"
    if len(Xs_indexes) == 2:
        i, j = Xs_indexes
        return (ys_values[j] - ys_values[i]) / (Xs_values[j] - Xs_values[i])
    return (f(Xs_indexes[1:], Xs_values, ys_values) - f(Xs_indexes[:-1], Xs_values, ys_values)) / (Xs_values[Xs_indexes[-1]] - Xs_values[Xs_indexes[0]])


def Newton_polynomial(x: np.ndarray, y: np.ndarray, x_eval: np.ndarray = None, info: bool = False) -> float | str:
    """Compute the Newton polynomial at given x_eval or print the polynomial to be evaluated at x_eval later.

    Args:
        x (np.ndarray): Interpolation nodes x
        y (np.ndarray): Interpolation nodes y
        x_eval (np.ndarray, optional): Array of x values to be evaluated at. Defaults to None.
        info (bool, optional): If True, print the polynomial and return it as a string. Defaults to False.

    Returns:
        float | str: Evaluated value or the polynomial as a string
    """
    if x_eval is not None:
        result = y[0]
        for i in range(1, x.shape[0]):
            temp = 1
            for xi in x[:i]:
                temp *= (x_eval - xi)
            result += f(np.arange(i + 1), x, y) * temp
    else:
        result = f"{y[0]}"
        for i in range(1, x.shape[0]):
            text = ""
            for xi in x[:i]:
                text += f" * (x - {xi})"
            result += " + " + str(f(np.arange(i + 1), x, y)) + text
        if info:
            print("P_n(x) = ", result, sep="", end="")
    return result


if __name__ == "__main__":
    def func(x):
        return 1 / np.sin(x)**2 - 1
    n = 10
    x = np.linspace(np.pi/6, np.pi/2, n)
    y = func(x)
    x_dense = np.linspace(np.pi/6, np.pi/2, int(1e4))
    x_dense = x_dense[~np.isin(x_dense, x)]
    print(Newton_polynomial(x, y, x_dense))

