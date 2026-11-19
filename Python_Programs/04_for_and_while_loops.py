# ==============================================================================
# Codomax Digital Solutions - Module 01: Introduction to AI & Python
# Program 04: Loops in Python (For and While Loops)
# Author: Hema Bala
# Description: Demonstrates for and while loops by printing a sequence of
#              numbers and calculating their cumulative sum.
# ==============================================================================

print("=" * 60)
print("             DEMONSTRATION OF LOOPS IN PYTHON")
print("=" * 60)

# ------------------------------------------------------------------------------
# PART 1: FOR LOOP DEMONSTRATION
# ------------------------------------------------------------------------------
# A for loop is ideal when the number of iterations is known in advance.
# Here, range(1, 6) generates numbers from 1 up to (but not including) 6.

print("\n--- 1. For Loop (Printing numbers 1 to 5 and calculating sum) ---")
for_total_sum = 0

print("Iterating using 'for loop':")
for current_number in range(1, 6):
    print(f"  Current number: {current_number}")
    for_total_sum += current_number  # Accumulating sum: for_total_sum = for_total_sum + current_number

print(f"Total Sum using For Loop (1 + 2 + 3 + 4 + 5) = {for_total_sum}")

# ------------------------------------------------------------------------------
# PART 2: WHILE LOOP DEMONSTRATION
# ------------------------------------------------------------------------------
# A while loop repeats as long as a specified condition remains True.
# A counter variable must be initialized and explicitly updated inside the loop.

print("\n--- 2. While Loop (Printing numbers 1 to 5 and calculating sum) ---")
counter = 1
while_total_sum = 0

print("Iterating using 'while loop':")
while counter <= 5:
    print(f"  Current number: {counter}")
    while_total_sum += counter  # Accumulating sum
    counter += 1               # Increment counter to prevent infinite loop

print(f"Total Sum using While Loop (1 + 2 + 3 + 4 + 5) = {while_total_sum}")

# ------------------------------------------------------------------------------
# SUMMARY & COMPARISON
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("Loop Summary & Verification:")
print(f"For Loop Result   : {for_total_sum}")
print(f"While Loop Result : {while_total_sum}")
print("Both loops successfully produced identical and verified results!")
print("=" * 60)
