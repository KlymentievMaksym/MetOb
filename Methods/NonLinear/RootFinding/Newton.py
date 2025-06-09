import numpy as np


def Newton(a: float, b: float, F: callable, Fs: callable, epsilon: float = 1e-6, info: bool = False, info_addition: bool = False, latex: bool = False) -> float:
    """Using Newton method

    Args:
        a (float): Left bound
        b (float): Right bound
        F (callable): Function
        Fs (callable): Derivation of Function (dF/dx)
        epsilon (float, optional): Error. Defaults to 1e-6.
        info (bool, optional): Print info. Defaults to False.
        info_addition (bool, optional): Print additional info. Defaults to False.
        latex (bool, optional): Using latex for print. Defaults to False.

    Returns:
        float: Root for function F
    """

    xk = a
    xk_1 = b

    count = 0

    if info:
        start = ""
        end = ""
        if latex:
            start = "$$ "
            end = " $$"
        text = "{start}[{count}] {Newton} [{a}, {b}]: {xk_}"
        text_end = "{start}[{count}] {Newton} [{a}, {b}]: {xk_}"
        if info_addition:
            text += " {start + end} |x_k - x_k-1| = |{xk} - {xk_1}| = {abs(xk - xk_1)} >= {epsilon}"
            text += " {start + end} |f(xk)| = |f({xk}| = {abs(F(xk))} >= {epsilon})"
            text_end += " {start + end} |x_k - x_k-1| = |{xk} - {xk_1}| = {abs(xk - xk_1)} < {epsilon}"
            text_end += " {start + or + end} |f(xk)| = |f({xk}| = {abs(F(xk))} < {epsilon})"
        text += "{end}"
        text_end += "{end}"

    while abs(xk - xk_1) >= epsilon or abs(F(xk)) >= epsilon:
        if info:
            xk_ = f"\\textbf{'{'}{xk}{'}'}" if latex else f"{xk}"
            dct = {
                "start": start,
                "end": end,
                "start + end": start + end,
                "count": count,
                "Newton": "Newton",
                "a": a,
                "b": b,
                "xk_": xk_,
                "xk": xk,
                "xk_1": xk_1,
                "abs(xk - xk_1)": abs(xk - xk_1),
                "abs(F(xk))": abs(F(xk)),
                "epsilon": epsilon
            }
            print(text.format(**dct))

        xk_1 = xk
        xk = xk - F(xk) / Fs(xk)
        xk = np.clip(xk, a, b)
        # xk = min(max(xk, a), b)
        count += 1

    if info:
        xk_ = f"\\textbf{'{'}{xk}{'}'}" if latex else f"{xk}"
        dct = {
            "start": start,
            "end": end,
            "start + end": start + end,
            "start + or + end": start + 'OR' + end,
            "count": count,
            "Newton": "\\textbf{Newton}" if latex else "Newton",
            "a": a,
            "b": b,
            "xk_": xk_,
            "xk": xk,
            "xk_1": xk_1,
            "abs(xk - xk_1)": abs(xk - xk_1),
            "abs(F(xk))": abs(F(xk)),
            "epsilon": epsilon
        }
        print(text_end.format(**dct))

    return xk


def Newton_from_poly_coefs(a: float, b: float, coefs: np.ndarray, epsilon: float = 1e-6) -> float:
    """Using Newton method

    Args:
        a (float): Left bound
        b (float): Right bound
        coefs (np.ndarray): polynoms' coefs
        epsilon (float, optional): Error. Defaults to 1e-6.

    Returns:
        float: Root for polynom with coefs
    """
    xk = a
    xk_1 = b

    count = 0

    while abs(xk - xk_1) >= epsilon or abs(np.polyval(coefs, xk)) >= epsilon:
        xk_1 = xk
        xk = xk - np.polyval(coefs, xk)/np.polyval(np.polyder(coefs), xk)
        xk = np.clip(xk, a, b)
        count += 1

    return xk


if __name__ == "__main__":
    def F(x):
        f = -2*x**4 + x**3 + 5*x**2 - 2*x + 7
        return f

    def F1(x):
        f = -8*x**3 + 3*x**2 + 10*x**1 - 2
        return f

    print(Newton(*[-2, -1.7], F, F1, info=False, info_addition=False, latex=False))
    print(Newton_from_poly_coefs(*[-2, -1.7], np.array([-2, 1, 5, -2, 7])))
