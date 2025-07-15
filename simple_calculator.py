# Simple Calculator in Python - CLI Version

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operation. Please choose +, -, *, or /."

print("🔢 Welcome to Simple Calculator")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose operation (+, -, *, /): ")

    result = calculate(num1, num2, operator)
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter valid numbers.")
