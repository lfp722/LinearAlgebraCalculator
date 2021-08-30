from DotProduct import dot_product

function_type = int(input("Type 1 for DotProduct: "))
if function_type == 1:
    dot_product()
else:
    raise ValueError("Not a proper number")