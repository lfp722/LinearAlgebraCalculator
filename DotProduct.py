import numpy as np


def dot_product() -> None:
    num_First_Row = int(input("Enter number of rows of first matrix: "))
    num_First_Column = int(input("Enter number of columns of first matrix: "))
    First_Matrix = [[0] * num_First_Column for a in range(num_First_Row)]

    num_Second_Row = int(input("Enter number of rows of second matrix: "))
    num_Second_Column = int(input("Enter number of columns of second matrix: "))
    Second_Matrix = [[0] * num_Second_Column for b in range(num_Second_Row)]

    i = 0
    while i < num_First_Row:
        j = 0
        while j < num_First_Column:
            First_Matrix[i][j] = float(input("Complete your first matrix: "))
            j += 1
        i += 1
    print(First_Matrix)

    i = 0
    while i < num_Second_Row:
        j = 0
        while j < num_Second_Column:
            Second_Matrix[i][j] = float(input("Complete your second matrix: "))
            j += 1
        i += 1
    print(Second_Matrix)
    print(np.dot(First_Matrix, Second_Matrix))
