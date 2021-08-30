from DotProduct import dot_product
from Determinant import determinant

function_type = int(input("Type 1 for DotProduct, 2 for determinant: "))
if function_type == 1:
    dot_product()

elif function_type == 2:
    determinant()

else:
    raise ValueError("Not a proper number")