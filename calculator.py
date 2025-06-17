# Function definitions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def floor_division(x, y):
    return x // y


def calculator():
    print("Python Calculator")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (x^y)")
        print("7. Floor Division (//)")

        choice = input("Enter your choice (1-7): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(x, y))
            elif choice == '2':
                print("Result:", subtract(x, y))
            elif choice == '3':
                print("Result:", multiply(x, y))
            elif choice == '4':
                print("Result:", divide(x, y))
            elif choice == '5':
                print("Result:", modulus(x, y))
            elif choice == '6':
                print("Result:", power(x, y))
            elif choice == '7':
                print("Result:", floor_division(x, y))
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

calculator()
