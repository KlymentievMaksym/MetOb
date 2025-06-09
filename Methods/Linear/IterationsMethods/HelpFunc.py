import numpy as np
from time import time


def if_diag_pan(matrix: np.ndarray, print_do: bool = False) -> bool:
    """
    Checks if the matrix is strictly diagonally dominant.

    Parameters
    ----------
    matrix : np.ndarray
        The matrix to check.
    print_do : bool, optional
        Whether to print the result or not. Defaults to False.

    Returns
    -------
    bool
        Whether the matrix is strictly diagonally dominant or not.
    """
    flag = True
    for row in range(matrix.shape[0]):
        flag &= abs(matrix[row, row]) >= sum(abs(matrix[row])) - abs(matrix[row, row])
    if print_do:
        print("Diag_Pan" if flag else "Not_Diag_Pan")
    return flag


def CreateCd(A: np.ndarray, b: np.ndarray, print_do: bool = False) -> tuple[np.ndarray, np.ndarray]:
    """
    Creates the matrices C and d for the simple iteration method.

    Parameters
    ----------
    A : np.ndarray
        The matrix of coefficients.
    b : np.ndarray
        The vector of free terms.
    print_do : bool, optional
        Whether to print the resulting matrices or not. Defaults to False.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        The matrices C and d.
    """
    assert if_diag_pan(A), "Matrix is not strictly diagonally dominant"
    C = np.zeros_like(A)
    d = np.zeros_like(b)
    for row in range(A.shape[0]):
        C[row] = (-A[row])/A[row, row]
        C[row, row] = 0
        d[row] = b[row]/A[row, row]
    if print_do:
        # for row in range(C.shape[0]):
        #     print(sum(abs(C[row])), sum(abs(C[:, row])))
        print(f"C[{row}]: {C[row]}")
        print(f"d[{row}]: {d[row]}")
    return C, d


def find_diag_pan_A(A: np.ndarray, time_out: int = 480) -> tuple[np.ndarray, np.ndarray, np.ndarray, bool]:
    """
    Finds a strictly diagonally dominant matrix A_ by randomly changing the elements of A.

    Parameters
    ----------
    A : np.ndarray
        The matrix.
    time_out : int, optional
        The time limit in seconds. Defaults to 480.

    Returns
    -------
    tuple[np.ndarray, np.ndarray, np.ndarray, bool]
        A_, unit, member, if_diag_pan(A_)
    """
    A_ = A.copy()
    unit = np.zeros(A.shape[1])  # 1 or 0?
    member = np.zeros(A.shape[1])  # 1 or 0?
    start_time = time()
    while not if_diag_pan(A_):
        A_ = A.copy()
        # Randomly generate a unit vector
        unit = np.random.uniform(-4, 4, A.shape[1])  # 1 or 0?
        # Randomly generate a vector of row indices
        member = np.random.choice(range(A.shape[0]), A.shape[1], replace=False)  # 1 or 0?
        # # Randomly generate a vector of row indices
        # member = np.random.randint(0, A_.shape[0], size=A.shape[1])
        # # Ensure that the row indices are not equal to the column indices
        # for member_index in range(member.shape[0]):
        #     while member[member_index] == member_index+1:
        #         member[member_index] = np.random.randint(0, A_.shape[0])
        # Perform the row operations
        A_[1] += A_[member[0]]*unit[0]
        A_[2] += A_[member[1]]*unit[1]
        A_[3] += A_[member[2]]*unit[2]
        A_[4] += A_[member[3]]*unit[3]
        # Check if the time limit has been exceeded
        if time_out > 0:
            if time() - start_time > time_out:
                print("Time out")
                return A_, unit, member, if_diag_pan(A_)
    return A_, unit, member, if_diag_pan(A_)
