"""
Simple Calculator
-----------------------
This program performs basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division.

It runs in a loop so the user can perform multiple calculations
until they choose to exit.
"""

# No extra imports needed since we're only using basic Python features

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the result of dividing two numbers.
       Includes handling for division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def main():
    """Main function that runs the calculator."""
    print("🧮 Welcome to the Simple Calculator!")
    print("You can perform addition, subtraction, multiplication, and division.")
    print("Type 'exit' anytime to quit.\n")

    # Infinite loop to keep the calculator running until user exits
    while True:
        # Take user input for the first number
        num1 = input("Enter the first number: ")

        # If the user types 'exit', stop the program
        if num1.lower() == "exit":
            print("👋 Thanks for using the calculator. Goodbye!")
            break

        # Validate that input is a number
        try:
            num1 = float(num1)  # Convert input to a number (supports decimals)
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")
            continue  # Skip rest of the loop and ask again

        # Take input for the operator (+, -, *, /)
        operator = input("Enter operation (+, -, *, /): ")

        # Check if the operator is valid
        if operator not in ["+", "-", "*", "/"]:
            print("⚠️ Invalid operator! Please choose from +, -, *, /.")
            continue

        # Take input for the second number
        num2 = input("Enter the second number: ")

        if num2.lower() == "exit":
            print("👋 Thanks for using the calculator. Goodbye!")
            break

        try:
            num2 = float(num2)
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")
            continue

        # Perform the chosen operation
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)

        # Display the result
        print(f"✅ Result: {num1} {operator} {num2} = {result}\n")


# The entry point of the program
# Ensures that main() runs only when the file is executed directly
if __name__ == "__main__":
    main()
