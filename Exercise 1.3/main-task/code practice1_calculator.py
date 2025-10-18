# Code Practice 1: If-Else Statements - Simple Calculator

# Get user inputs
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
operator = input("Enter the operator (+ or -): ")

# Use if-elif-else to perform the operation
if operator == "+":
    result = value1 + value2
    print(f"Result: {value1} + {value2} = {result}")

elif operator == "-":
    result = value1 - value2
    print(f"Result: {value1} - {value2} = {result}")

else:
    print("Unknown operator")