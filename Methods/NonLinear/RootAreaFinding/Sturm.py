import numpy as np


def polyval(coefs: np.ndarray, X: np.ndarray) -> np.ndarray[float]:
    """
    Returns value for polynom with exact X-es. coefs[0] + coefs[1]*x + coefs[2]*x**2 + ... = np.ndarray[float]

    Parameters
    ----------
    coefs : np.ndarray
        float coefs before X-es
    X : np.ndarray
        floats to calculate

    Returns
    -------
    np.ndarray[float]
        result from polynom with exact X-es
    """
    n = len(coefs)
    degrees = np.arange(n-1, -1, -1)
    res = np.zeros(len(X))
    for x_index in range(len(X)):
        for degree_index in range(len(degrees)):
            res[x_index] += coefs[degree_index] * X[x_index]**degrees[degree_index]
    return res


def Sturm(coefs: np.ndarray, interval_of_finding: list[float] = [-10, 10], dots_count: int = 30) -> list[list[float]]:
    """
    Using Sturm method to find roots of polynomials

    Parameters
    ----------
    coefs : np.ndarray
        float coefs before X-es. coefs[0] + coefs[1]*x + coefs[2]*x**2 + ... = float
    interval_of_finding : list[float], optional
        Interval where roots can be. Defaults to [-10, 10].
    dots_count : int, optional
        Amount of dots in interval (can be interpreted as how big step is between dots). Defaults to 30.

    Returns
    -------
    list[list[float]]
        Intervals where roots are (if dots_count is small or interval_of_finding is small there can be no roots or more than one)
    """
    dots_count = int(dots_count)
    intervals = []
    n = len(coefs)
    polys = [coefs, np.polyder(coefs)]
    for i in range(1, n-1):
        polys.append(-np.polydiv(polys[i-1], polys[i])[1])

    X = np.linspace(*interval_of_finding, dots_count)
    matrix = np.zeros((len(polys), len(X)))
    for poly_index in range(len(polys)):
        matrix[poly_index] = np.polyval(polys[poly_index], X)

    sign_change = np.sum(np.diff(np.sign(matrix.T), axis=1) != 0, axis=1)
    difference = np.diff(sign_change, axis=0) != 0
    for diff_index in range(len(difference)):
        if difference[diff_index]:
            intervals.append([X[diff_index], X[diff_index+1]])
    return intervals


if __name__ == "__main__":
    coefs = np.array([26.8, -256.2267, 1031.97237, -1465.66094076])
    coef = np.array([1, *(-coefs)])
    intervals = Sturm(coef, interval_of_finding=[-100, 100], dots_count=1e3)
    print(*intervals)
