import numpy as np

# TODO: REDO LAST PART
def TheoremLagrange(f_coefs: np.ndarray, interval_of_finding: list[float] = [-10, 10], dots_count: int = 30):
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

    x = np.linspace(*interval_of_finding, dots_count)
    for coef_index in range(len(coefs)):
        coef = coefs[coef_index]
        print(coef)
        n = len(coef) - 1
        negative_first = [[coef[0], n]]
        for i in range(1, len(coef)):
            if coef[i] < 0:
                negative_first.append([coef[i], n - i])
        f = np.zeros_like(x)
        for x_index in range(len(x)):
            for i in range(len(negative_first)):
                f[x_index] += negative_first[i][0] * x[x_index] ** negative_first[i][1]
            # print(x_, f)
            # if f >= 0:
                # intervals[*dct[coef_index]] = x_
                # break
        # result = np.min(f[f > 0])
        print(np.where(f > 0, f, np.inf))
        x_ = x[np.argmin(np.where(f > 0, f, np.inf))]
        print(x_)
        intervals[*dct[coef_index]] = dct2[coef_index][0] * x_ ** dct2[coef_index][1]
    return intervals


if __name__ == '__main__':
    f_coefs = np.array([-2, 1, 5, -2, 7])
    print(TheoremLagrange(f_coefs, interval_of_finding=[-4, 4], dots_count=30))
