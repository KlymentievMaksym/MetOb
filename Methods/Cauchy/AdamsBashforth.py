import numpy as np

if __name__ == "__main__":
    from RungeKutta import runge_kutta_4
else:
    from .RungeKutta import runge_kutta_4


def adams_bashforth_4(x_init: np.ndarray, y_init: np.ndarray, h: float, n: int, f_s: callable) -> tuple[np.ndarray, np.ndarray]:
    """Адамс-Башфорт четвертого порядку

    Args:
        x_init (np.ndarray): 4 або більше елементів по x
        y_init (np.ndarray): 4 або більше елементів по y
        h (float): Крок
        n (int): Кількість точок
        f_s (callable): Функція похідної

    Returns:
        tuple[np.ndarray, np.ndarray]: Масиви x та y
    """
    assert x_init.shape[0] >= 4, f"x_init.shape[0] must be >= 4, received {x_init.shape[0]}"
    assert y_init.shape[0] >= 4, f"y_init.shape[0] must be >= 4, received {y_init.shape[0]}"
    x = np.zeros(n)
    y = np.zeros(n)
    x[:4] = x_init[:4]
    y[:4] = y_init[:4]
    for i in range(3, n-1):
        f_n = f_s(x[i],   y[i])
        f_n1 = f_s(x[i-1], y[i-1])
        f_n2 = f_s(x[i-2], y[i-2])
        f_n3 = f_s(x[i-3], y[i-3])

        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*(55*f_n - 59*f_n1 + 37*f_n2 - 9*f_n3)/24
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
    x_rk, y_rk = runge_kutta_4(x0, y0, h, n, f_s)
    x, y = adams_bashforth_4(x_rk, y_rk, h, n, f_s)
    print(x, y)
