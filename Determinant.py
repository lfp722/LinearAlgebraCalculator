import numpy as np


def determinant() -> None:
    num_row = int(input("Enter number of rows: "))
    num_col = int(input("Enter number of columns: "))
    Matrix = [[0] * num_col for a in range(num_row)]

    i = 0
    while i < num_row:
        j = 0
        while j < num_col:
            Matrix[i][j] = float(input("Complete your matrix: "))
            j += 1
        i += 1
    print(Matrix)
    print("------Determinant------")
    print(np.linalg.det(Matrix))