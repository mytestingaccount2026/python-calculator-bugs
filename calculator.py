"""
Simple Calculator with Intentional Bugs
This calculator has several bugs that need to be fixed!
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    # BUG 1: Wrong operation - returns addition instead of subtraction
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    # BUG 3: Uses multiplication instead of power operation
    return a * b

def modulo(a, b):
    """Return remainder of a divided by b"""
    return a % b

def main():
    """Main calculator interface"""
    print("Simple Calculator")
    print("=" * 40)
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("0. Exit")

    while True:
        try:
            # BUG 4: Input is not validated properly - crashes on non-numeric input
            choice = int(input("\nEnter operation (0-6): "))

            if choice == 0:
                print("Goodbye!")
                break

            if choice < 1 or choice > 6:
                print("Invalid choice. Please select 1-6.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            elif choice == 5:
                result = power(num1, num2)
                print(f"Result: {num1} ^ {num2} = {result}")
            elif choice == 6:
                result = modulo(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")

        except ValueError:
            # BUG 5: Error message is misleading and does not help user
            print("Error occurred!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
