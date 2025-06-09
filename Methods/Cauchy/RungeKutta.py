import numpy as np


def runge_kutta_4(x0: float, y0: float, h: float, n: int, f_s: callable) -> tuple[np.ndarray, np.ndarray]:
    """Рунге-Кутта четвертого порядку

    Args:
        x0 (float): Початкова точка по x
        y0 (float): Початкова точка по y
        h (float): Крок
        n (int): Кількість точок
        f_s (callable): Функція похідної

    Returns:
        tuple[np.ndarray, np.ndarray]: Масиви x та y
    """
    assert n > 0, f"n must be > 0, received {n}"
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(n-1):
        x_i = x[i]
        y_i = y[i]

        k1 = h * f_s(x_i, y_i)
        k2 = h * f_s(x_i + h/2, y_i + 1/2*k1)
        k3 = h * f_s(x_i + h/2, y_i + 1/2*k2)
        k4 = h * f_s(x_i + h, y_i + k3)

        x[i+1] = x_i + h
        y[i+1] = y_i + (k1 + 2*k2 + 2*k3 + k4)/6
    return x, y


if __name__ == "__main__":
    def f(x):
        return x * np.sin(x)

    def f_s(x, y):
        # y'(x) = sin(x) + x cos(x)
        # sin(x) + x cos(x) = (1 - x * sin(x)) * x**2 + F(x)
        # F(x) = sin(x) + x * cos(x) - (1 - x * sin(x)) * x**2
        Fx = np.sin(x) + x * np.cos(x) - (1 - x * np.sin(x)) * x**2
        return (1 - y)*x**2 + Fx
    n = 45
    h = 0.1
    x0 = 0
    y0 = f(x0)
    x0, y0
    x, y = runge_kutta_4(x0, y0, h, n, f_s)
    print(x, y)
