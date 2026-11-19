# ==============================================================================
# Codomax Digital Solutions - Module 01: Introduction to AI & Python
# Program 03: Conditional Statements (Student Grading System)
# Author: Hema Bala
# Description: Accepts student marks, validates the input range (0 to 100),
#              and determines the grade using if, elif, and else statements.
# ==============================================================================

def evaluate_student_grade(marks):
    """
    Evaluates student marks and returns the corresponding grade.
    Validates that marks must fall between 0 and 100 inclusive.
    """
    # Input validation: check whether marks are within the valid range [0, 100]
    if marks < 0 or marks > 100:
        return "Invalid Marks! Marks must be between 0 and 100."
    elif marks >= 90:
        return "Grade A+ (Outstanding Performance)"
    elif marks >= 80:
        return "Grade A (Excellent Performance)"
    elif marks >= 70:
        return "Grade B (Good Performance)"
    elif marks >= 60:
        return "Grade C (Above Average)"
    elif marks >= 50:
        return "Grade D (Pass)"
    else:
        return "Grade F (Needs Improvement / Fail)"


def main():
    print("=" * 60)
    print("       STUDENT GRADING SYSTEM - CONDITIONAL STATEMENTS")
    print("=" * 60)

    try:
        user_input = input("Enter student marks (0 to 100): ").strip()
        marks = float(user_input)

        # Evaluate and display result
        grade_result = evaluate_student_grade(marks)
        print("-" * 60)
        print(f"Entered Marks : {marks}")
        print(f"Result / Grade: {grade_result}")
        print("-" * 60)

    except ValueError:
        print("\n[Input Error]: Please enter a valid numeric value for marks.")


if __name__ == "__main__":
    main()
