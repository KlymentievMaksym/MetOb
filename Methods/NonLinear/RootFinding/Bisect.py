def Bisect(a: float, b: float, F: callable, epsilon: float = 1e-6, info: bool = False, info_addition: bool = False, latex: bool = False) -> float:
    """Using bisect method

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
    count = 0

    if info:
        start = ""
        end = ""
        if latex:
            start = "$$ "
            end = " $$"
        text = "{start}[{count}] {Bisect} [{a}, {b}]: {c_}"
        text_end = "{start}[{count}] {Bisect} [{a}, {b}]: {c_}"
        if info_addition:
            text += " {start + end} |a - b| = |{a} - {b}| = {abs(a-b)} >= {epsilon}"
            text_end += " {start + end} |a - b| = |{a} - {b}| = {abs(a-b)} < {epsilon}"
        text += "{end}"
        text_end += "{end}"

    while abs(a - b) >= epsilon:
        c = (a + b) / 2

        if info:
            c_ = f"\\textbf{'{'}{c}{'}'}" if latex else f"{c}"
            dct = {
                "start": start,
                "end": end,
                "start + end": start + end,
                "count": count,
                "Bisect": "Bisect",
                "a": a,
                "b": b,
                "c_": c_,
                "abs(a-b)": abs(a-b),
                "epsilon": epsilon
            }
            print(text.format(**dct))

        if F(a) * F(c) <= 0:
            b = c
        elif F(b) * F(c) <= 0:
            a = c

        count += 1

    if info:
        c_ = f"\\textbf{'{'}{c}{'}'}" if latex else f"{c}"
        dct = {
            "start": start,
            "end": end,
            "start + end": start + end,
            "count": count,
            "Bisect": "\\textbf{Bisect}" if latex else "Bisect",
            "a": a,
            "b": b,
            "c_": c_,
            "abs(a-b)": abs(a-b),
            "epsilon": epsilon
        }
        print(text_end.format(**dct))
    return (a + b)/2


if __name__ == "__main__":
    def F(x):
        f = -2*x**4 + x**3 + 5*x**2 - 2*x + 7
        return f
    print(Bisect(*[-2, -1.7], F, info=False, info_addition=False, latex=False))
