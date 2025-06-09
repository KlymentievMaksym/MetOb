import numpy as np


def TheoremUpperBound(f_coefs: np.ndarray):
    coefs = np.array([f_coefs, f_coefs[::-1], np.append(-f_coefs[:-1], f_coefs[-1]), np.append(f_coefs[-1], -f_coefs[:-1][::-1])])
    for i in range(len(coefs)):
        if coefs[i][0] < 0:
            coefs[i] = -coefs[i]
    intervals = np.array([[0, 0], [0, 0]], dtype=float)

    dct = {
        0: [0, 1],
        1: [0, 0],
        2: [1, 0],
        3: [1, 1]
    }

    dct2 = {
        0: [1, 1],
        1: [1, -1],
        2: [-1, 1],
        3: [-1, -1]
    }

    for coef_index in range(len(coefs)):
        coef = coefs[coef_index]
        n = len(coef) - 1
        a_n = coef[0]
        max_negative = np.max(np.abs(coef[coef < 0]))
        m = n - np.argmax(coef < 0)
        R = 1 + (max_negative / a_n) ** 1/(n - m)
        intervals[*dct[coef_index]] = dct2[coef_index][0] * R ** dct2[coef_index][1]
    return intervals


if __name__ == '__main__':
    f_coefs = np.array([-2, 1, 5, -2, 7])
    print(TheoremUpperBound(f_coefs))
