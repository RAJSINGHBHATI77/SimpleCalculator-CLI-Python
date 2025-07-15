# ✨ Simple Calculator with Modular Functions and Error Handling

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("\n🔢 Welcome to the Simple Calculator!")
    print("Operations Available:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")

    operation = input("Enter operation (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        print("❌ Invalid operation. Please choose from +, -, *, /.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operation_func = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }

        result = operation_func[operation](num1, num2)
        print(f"✅ Result: {result}")

    except ValueError:
        print("❌ Error: Please enter valid numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
