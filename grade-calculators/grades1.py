"""
PURPOSE: Calculates your grade for a course where the course has four
equally-weighted assignments. Each assignment is graded out of 50 points. No
fractional points on assignments.

AUTHOR: Amber Morgan
"""

def main():
    grade1 = int(input("Grade 1 out of 50: "))
    grade2 = int(input("Grade 2 out of 50: "))
    grade3 = int(input("Grade 3 out of 50: "))
    grade4 = int(input("Grade 4 out of 50: "))
    grade1 = grade1 / 50
    grade2 = grade2 / 50
    grade3 = grade3 / 50
    grade4 = grade4 / 50
    final_grade = (grade1 + grade2 + grade3 + grade4) / 4
    final_grade = int(final_grade * 100)
    print("Final Grade is", final_grade, "out of 100")

if __name__ == "__main__":
    main()
