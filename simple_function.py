
a = int(input("Type the first number: "))
b = int(input("Type the second number: "))


def operation(a, b):
    op = int(input(f"""
    {50 * "*"}\n
    Type the kind of operation you desire to do:\n
    Addition ----- 1\n
    Subtraction ----- 2\n
    Multiplication ----- 3\n
    Division ----- 4\n
    """))
    if (op == 1):
        return (f"Addition of {a} and {b} is: {a+b}.")
    if (op == 2):
        return (f"Subtraction of {a} and {b} is: {a-b}.")
    if (op == 3):
        return (f"Multiplication of {a} and {b} is: {a*b}.")
    if (op == 4):
        return (f"Division of {a} and {b} is: {a/b}.")


print(operation(a, b))
