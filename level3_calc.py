def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def calculator():
    """Simple CLI calculator."""
    print("\nSimple Calculator")
    print("Operations: +  -  *  /")

    while True:
        op = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if op == 'q':
            print("Exiting calculator.")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if op == '+':
            print("Result:", add(a, b))
        elif op == '-':
            print("Result:", subtract(a, b))
        elif op == '*':
            print("Result:", multiply(a, b))
        elif op == '/':
            print("Result:", divide(a, b))
        else:
            print("Invalid operation!")


# Run calculator
calculator()