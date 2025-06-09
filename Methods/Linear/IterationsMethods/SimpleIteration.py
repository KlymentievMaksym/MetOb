import numpy as np

if __name__ == "__main__":
    from HelpFunc import CreateCd
else:
    from .HelpFunc import CreateCd


def Iteration_simple_method(C: np.ndarray, d: np.ndarray, epsilon: float = 1e-4, print_do: bool = False, A_start: np.ndarray = None, b_start: np.ndarray = None) -> np.ndarray:
    """
    Performs the simple iteration method for solving linear systems of equations.

    Args:
        C (np.ndarray): The iteration matrix.
        d (np.ndarray): The constant vector.
        epsilon (float, optional): The convergence tolerance. Defaults to 1e-4.
        print_do (bool, optional): If True, prints intermediate results. Defaults to False.
        A_start (np.ndarray, optional): The initial coefficient matrix for calculating residuals.
        b_start (np.ndarray, optional): The initial constant vector for calculating residuals.

    Returns:
        np.ndarray: The solution vector.
    """
    # Initialize the solution vector with zeros
    xk = np.zeros(d.shape)
    xk1 = C @ xk + d

    count = 0

    # Optionally print the initial residual and solution
    if print_do:
        r = abs(b_start - A_start @ xk1)
        print(f"[{count}] r: \n {r} \n")
        print(f"[{count}] x: \n {xk1} \n\n")

    # Calculate the convergence factor q
    q = np.zeros(d.shape)
    for row in range(C.shape[0]):
        q = min(sum(abs(C[row])), sum(abs(C[:, row])))

    # Iterate until convergence
    while q / (1 - q) * np.max(abs(xk1 - xk)) >= epsilon:
        xk = xk1
        xk1 = C @ xk + d

        count += 1

        # Optionally print the current residual and solution
        if print_do:
            r = abs(b_start - A_start @ xk1)
            print(f"[{count}] r: \n {r} \n")
            print(f"[{count}] x: \n {xk1} \n\n")

    return xk1


if __name__ == "__main__":
    A = np.array([
        [6.59, 1.28, 0.79, 1.195, -0.21],
        [0.92, 3.83, 1.3, -1.63, 1.02],
        [1.15, -2.46, 5.77, 2.1, 1.483],
        [1.285, 0.16, 2.1, 5.77, -18],
        [0.69, -1.68, -1.217, 9, -6]
    ])
    b = np.array([
        [2.1],
        [0.36],
        [3.89],
        [11.04],
        [-0.27]
    ])
    A_start = A.copy()
    b_start = b.copy()

    A[1] += A[4]*1/4
    b[1] += b[4]*1/4
    A[2] += A[1]*0.8
    b[2] += b[1]*0.8
    A[3] += A[4]*-2.28
    b[3] += b[4]*-2.28
    A[4] += A[3]*0.4
    b[4] += b[3]*0.4

    C, d = CreateCd(A, b, print_do=False)

    x = Iteration_simple_method(C, d)

    print(A_start @ x)
    print(b_start)
