import numpy as np


def TheoremAllRoots(polynom_coefs: np.ndarray) -> np.ndarray:
    """Takes polynom coefs and returns where all |roots| are

    Args:
        polynom_coefs (np.ndarray): From high to low

    Returns:
        np.ndarray: Where all |roots| are
    """
    A = np.max(polynom_coefs[1:])
    B = np.max(polynom_coefs[:-1])
    a0 = np.abs(polynom_coefs[-1])
    an = np.abs(polynom_coefs[0])
    left = a0/(B + a0)
    right = (an + A)/an
    return np.array([[left, right], [-right, -left]])


if __name__ == '__main__':
    f_coefs = np.array([-2, 1, 5, -2, 7])
    print(TheoremAllRoots(f_coefs))
