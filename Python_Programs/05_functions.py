# ==============================================================================
# Codomax Digital Solutions - Module 01: Introduction to AI & Python
# Program 05: Reusable Arithmetic Functions
# Author: Hema Bala
# Description: Demonstrates functions for basic arithmetic operations
#              (addition, subtraction, multiplication, division) and handles
#              division by zero error safely.
# ==============================================================================

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2


def divide(num1, num2):
    """
    Returns the quotient of dividing num1 by num2.
    Safely checks and handles division by zero.
    """
    if num2 == 0:
        return "Error: Division by zero is not permitted!"
    return num1 / num2


def main():
    print("=" * 65)
    print("      DEMONSTRATION OF REUSABLE FUNCTIONS & ARITHMETIC")
    print("=" * 65)

    # Sample input values
    first_number = 20
    second_number = 4

    print(f"Initial operands: first_number = {first_number}, second_number = {second_number}\n")

    # Calling each function
    add_result = add(first_number, second_number)
    sub_result = subtract(first_number, second_number)
    mul_result = multiply(first_number, second_number)
    div_result = divide(first_number, second_number)

    print(f"Addition       : {first_number} + {second_number} = {add_result}")
    print(f"Subtraction    : {first_number} - {second_number} = {sub_result}")
    print(f"Multiplication : {first_number} * {second_number} = {mul_result}")
    print(f"Division       : {first_number} / {second_number} = {div_result}")

    # Demonstrating error handling for division by zero
    print("\n" + "-" * 65)
    print("Demonstrating Zero Division Handling:")
    print("-" * 65)
    zero_divisor = 0
    zero_division_result = divide(first_number, zero_divisor)
    print(f"Attempting: {first_number} / {zero_divisor}")
    print(f"Output    : {zero_division_result}")
    print("=" * 65)


if __name__ == "__main__":
    main()
