# Task 2: Calculator

print("Welcome to Simple Calculator!")

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
print("\nChoose an operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operation = input("Enter your choice (+, -, *, /): ")

# Perform the selected calculation
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation. Please choose +, -, *, or /.")
