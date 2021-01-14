
try:
    a = float(input("Type the first number: "))
    b = float(input("Type the second number: "))

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
except ValueError:
    print(f"""
    {50 * "*"}\n
    Sorry, the character typed is not a number.\n
    Please enter a valid number.
    """)
except ZeroDivisionError:
    print(f"""
    {50 * "*"}\n
    Sorry, you can't divide a number by 0.\n
    Please enter a valid number.
    """)
except AssertionError:
    print(f"""
{50 * "*"}\n
    Sorry, an unexpected error occurred.\n
    Please, try again...
    """)
