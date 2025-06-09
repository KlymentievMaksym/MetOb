import numpy as np
import RootFinding as RF
import RootAreaFinding as RA

def F(x):
    f = -2*x**4 + x**3 + 5*x**2 - 2*x + 7
    return f


def Fs(x):
    f = -8*x**3 + 3*x**2 + 10*x**1 - 2
    return f


f_coefs = np.array([-2, 1, 5, -2, 7])
fs_coefs = np.array([-8, 3, 10, -2])

interval_1 = RA.TheoremAllRoots(f_coefs)
interval_2 = RA.TheoremUpperBound(f_coefs)
print(interval_1)
print(interval_2)

# print(RF.Newton(*[-2, -1.7], F, Fs, info=False, info_addition=False, latex=False))
# print(RF.Newton_from_poly_coefs(*[-2, -1.7], np.array([-2, 1, 5, -2, 7])))
