import math

def calculator():
    print("\n===== ADVANCED CALCULATOR =====")

    while True:
        print("\nSelect Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Calculator Closed.")
            break

        try:
            if choice == '7':
                num = float(input("Enter number: "))

                if num < 0:
                    print("Cannot calculate square root of negative number.")
                else:
                    print("Result =", math.sqrt(num))

            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result =", num1 + num2)

                elif choice == '2':
                    print("Result =", num1 - num2)

                elif choice == '3':
                    print("Result =", num1 * num2)

                elif choice == '4':
                    if num2 == 0:
                        print("Division by zero not allowed.")
                    else:
                        print("Result =", num1 / num2)

                elif choice == '5':
                    print("Result =", num1 ** num2)

                elif choice == '6':
                    print("Result =", num1 % num2)

                else:
                    print("Invalid Choice")

        except ValueError:
            print("Please enter valid numbers.")

calculator()