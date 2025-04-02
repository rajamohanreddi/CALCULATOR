def calculator():
    print("Welcome to the Simple Calculator!")
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation symbol (+, -, *, /): ")
    if operation == "+":
        r = n1 + n2
    elif operation == "-":
        r = n1 - n2
    elif operation == "*":
        r = n1 * n2
    elif operation == "/":
        if n2 != 0:
            r = n1 / n2
        else:
            print("Error! Division by zero is not allowed.")
            return
    else:
        print("Invalid operation! Please choose a valid symbol (+, -, *, /).")
        return
    print(f"\nThe result of {n1} {operation} {n2} is: {r}")
calculator()
