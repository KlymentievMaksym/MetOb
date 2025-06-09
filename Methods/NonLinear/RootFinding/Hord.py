def Hord(a: float, b: float, F: callable, epsilon: float = 1e-6, info: bool = False, info_addition: bool = False, latex: bool = False) -> float:
    """Using hord method

    Args:
        a (float): Left bound
        b (float): Right bound
        F (callable): Function
        epsilon (float, optional): Error. Defaults to 1e-6.
        info (bool, optional): Print info. Defaults to False.
        info_addition (bool, optional): Print additional info. Defaults to False.
        latex (bool, optional): Using latex for print. Defaults to False.

    Returns:
        float: Root for function F
    """

    c = (a * F(b) - b * F(a)) / (F(b) - F(a))
    c_prev = 0

    count = 0

    if info:
        start = ""
        end = ""
        if latex:
            start = "$$ "
            end = " $$"
        text = "{start}[{count}] {Hord} [{a}, {b}]: {c_}"
        text_end = "{start}[{count}] {Hord} [{a}, {b}]: {c_}"
        if info_addition:
            text += " {start + end} |c - c_prev| = |{c} - {c_prev}| = {abs(c - c_prev)} >= {epsilon}"
            text += " {start + end} |f(c)| = |f({c}| = {abs(F(c))} >= {epsilon}"
            text_end += " {start + end} |c - c_prev| = |{c} - {c_prev}| = {abs(c - c_prev)} < {epsilon}"
            text_end += " {start + or + end} |f(c)| = |f({c}| = {abs(F(c))} < {epsilon}"
        text += "{end}"
        text_end += "{end}"

    while abs(c - c_prev) >= epsilon or abs(F(c)) >= epsilon:
        c = (a*F(b) - b*F(a))/(F(b) - F(a))

        if info:
            c_ = f"\\textbf{'{'}{c}{'}'}" if latex else f"{c}"
            dct = {
                "start": start,
                "end": end,
                "start + end": start + end,
                "count": count,
                "Hord": "Hord",
                "a": a,
                "b": b,
                "c_": c_,
                "c": c,
                "c_prev": c_prev,
                "abs(c - c_prev)": abs(c - c_prev),
                "abs(F(c))": abs(F(c)),
                "epsilon": epsilon
            }
            print(text.format(**dct))

        if F(a)*F(c) <= 0:
            b = c
        elif F(b)*F(c) <= 0:
            a = c

        c_prev = c
        count += 1

    if info:
        c_ = f"\\textbf{'{'}{c}{'}'}" if latex else f"{c}"
        dct = {
            "start": start,
            "end": end,
            "start + end": start + end,
            "start + or + end": start + 'OR' + end,
            "count": count,
            "Hord": "\\textbf{Hord}" if latex else "Hord",
            "a": a,
            "b": b,
            "c_": c_,
            "c": c,
            "c_prev": c_prev,
            "abs(c - c_prev)": abs(c - c_prev),
            "abs(F(c))": abs(F(c)),
            "epsilon": epsilon
        }
        print(text_end.format(**dct))
    return (a * F(b) - b * F(a)) / (F(b) - F(a))


if __name__ == "__main__":
    def F(x):
        f = -2*x**4 + x**3 + 5*x**2 - 2*x + 7
        return f
    print(Hord(*[-2, -1.7], F, info=False, info_addition=False, latex=False))
