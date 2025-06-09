import numpy as np


def latex_matrix(matrix: np.ndarray) -> str:
    """
    Convert a numpy matrix to a latex string.
    """
    matrix_ = matrix.copy()
    text = "$\n"
    text += r"\left(\begin{matrix}" + "\n"
    for row in matrix_:
        text += " "*4 + " & ".join(map(str, row)) + r" \\" + "\n"
    text += r"\end{matrix}\right)"
    text += "\n$"
    return text


def Danilevsky(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Danilevsky's method for finding the coefs of polynom except highest degree to find eigenvalues and matrix to receive eigenvectors of a matrix.

    Args:
        matrix (np.ndarray): The matrix to find the coefs of polynom except highest degree to find eigenvalues and matrix to receive eigenvectors of.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple containing the coefs of polynom except highest degree to find eigenvalues and matrix to receive eigenvectors of the matrix.
    """
    n = len(matrix)
    Ps = np.zeros((n, n, n))
    Ps[-1] = matrix.copy()
    Ms = np.array(list(np.identity(n)for i in range(n-1)))
    Ms_1 = np.array(list(np.identity(n)for i in range(n-1)))
    M = None
    for k in range(n-2, -1, -1):
        Ms[k][k] = -Ps[k+1][k+1] / Ps[k+1][k+1][k]
        Ms[k][k][k] = -Ms[k][k][k] / Ps[k+1][k+1][k]
        Ms_1[k][k] = Ps[k+1][k+1]

        # index = k + 1
        # print(f"$A_{index} = $", latex_matrix(np.round(Ps[k+1], 4)) + "\n", r"$M^{-1}" + f"_{index} = $", latex_matrix(np.round(Ms_1[k], 4)) + "\n", f"$M_{index} = $", latex_matrix(np.round(Ms[k], 4)) + "\n", sep='\n')

        Ps[k] = Ms_1[k] @ Ps[k+1] @ Ms[k]
        if M is None:
            M = Ms[k]
        else:
            M @= Ms[k]

    # print(f"$A_{0} = P = $", latex_matrix(np.round(Ps[0], 4)) + "\n", sep='\n')
    return Ps[0][0], M


if __name__ == '__main__':
    matrix = np.array([
        [2.2, 1, 0.5, 2],
        [1, 1.3, 2, 1],
        [0.5, 2, 0.5, 1.6],
        [2, 1, 1.6, 2]
    ])
    coefs, M = Danilevsky(matrix)
    print(coefs)
