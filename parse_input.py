# Hack hack hack
# because we can't use symbols as filenames
def parse_input(op):
    if op == "+":
        return "plus"
    elif op == "-":
        return "minus"
    elif op == "*":
        return "multiply"
    elif op == "/":
        return "divide"
    raise NotImplementedError
