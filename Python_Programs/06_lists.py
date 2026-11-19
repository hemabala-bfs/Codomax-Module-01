# ==============================================================================
# Codomax Digital Solutions - Module 01: Introduction to AI & Python
# Program 06: Python Lists Operations
# Author: Hema Bala
# Description: Demonstrates list creation, append(), remove(), sort(),
#              list iteration using a loop, and computing the average mark.
# ==============================================================================

print("=" * 65)
print("             DEMONSTRATION OF LIST OPERATIONS IN PYTHON")
print("=" * 65)

# 1. Initializing a list of student marks
student_marks = [85, 92, 78, 64, 88]
print(f"1. Initial List of Marks           : {student_marks}")

# 2. Appending a new mark to the list using append()
new_mark = 95
student_marks.append(new_mark)
print(f"2. After appending {new_mark}              : {student_marks}")

# 3. Removing a specific mark from the list using remove()
mark_to_remove = 64
student_marks.remove(mark_to_remove)
print(f"3. After removing mark {mark_to_remove}          : {student_marks}")

# 4. Sorting the list in ascending order using sort()
student_marks.sort()
print(f"4. After sorting in ascending order : {student_marks}")

# 5. Iterating through the list using a for loop
print("\n5. Iterating through student marks:")
for index, mark in enumerate(student_marks, start=1):
    print(f"   Subject {index} Mark: {mark}")

# 6. Calculating the total sum and average mark
total_marks = sum(student_marks)
total_subjects = len(student_marks)
average_mark = total_marks / total_subjects

print("\n" + "-" * 65)
print(f"Total Subjects Count : {total_subjects}")
print(f"Sum of Marks         : {total_marks}")
print(f"Calculated Average   : {average_mark:.2f}")
print("=" * 65)
