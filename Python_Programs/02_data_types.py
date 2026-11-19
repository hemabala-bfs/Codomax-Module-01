# ==============================================================================
# Codomax Digital Solutions - Module 01: Introduction to AI & Python
# Program 02: Basic Data Types in Python
# Author: Hema Bala
# Description: Demonstrates fundamental data types (int, float, str, bool)
#              and inspects their types using Python's built-in type() function.
# ==============================================================================

# 1. Integer (int): Whole numbers without decimal points
student_roll_no = 101

# 2. Floating-point number (float): Numbers with fractional/decimal parts
cgpa_score = 8.75

# 3. String (str): Sequence of characters enclosed in quotes
student_name = "Hema Bala"

# 4. Boolean (bool): Binary logical values (True or False)
is_enrolled = True

# Displaying each variable's value along with its data type
print("=" * 60)
print("         DEMONSTRATION OF PYTHON BASIC DATA TYPES")
print("=" * 60)

print(f"Value: {student_roll_no:<15} | Type: {type(student_roll_no)}")
print(f"Value: {cgpa_score:<15} | Type: {type(cgpa_score)}")
print(f"Value: {student_name:<15} | Type: {type(student_name)}")
print(f"Value: {str(is_enrolled):<15} | Type: {type(is_enrolled)}")

print("=" * 60)
print("Summary of demonstrated data types:")
print(f"- {student_roll_no} is an integer (int)")
print(f"- {cgpa_score} is a floating-point number (float)")
print(f"- '{student_name}' is a string of text (str)")
print(f"- {is_enrolled} is a boolean truth value (bool)")
print("=" * 60)
