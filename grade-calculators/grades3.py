"""
PURPOSE: Calculates your grade for a course where the course has:
  * 2 exams
  * 4 assignments
Each exam is out of 100 points and equally weighted. Overall the exams are
worth 25% of the final grade. Each assignment is graded out of 50 points and
equally weighted and worth 75% of the overall grade. No fractional points on
exams or assignments.

AUTHOR: Amber Morgan
"""

def main():
    exam1 = int(input("Exam Grade 1 out of 100: "))
    exam2 = int(input("Exam Grade 2 out of 100: "))
    assignment1 = int(input("Assignment Grade 1 out of 50: "))
    assignment2 = int(input("Assignment Grade 2 out of 50: "))
    assignment3 = int(input("Assignment Grade 3 out of 50: "))
    assignment4 = int(input("Assignment Grade 4 out of 50: "))
    exam1 = exam1 / 100
    exam2 = exam2 / 100
    assignment1 = assignment1 / 50
    assignment2 = assignment2 / 50
    assignment3 = assignment3 / 50
    assignment4 = assignment4 / 50
    assignments = ((assignment1 + assignment2 + assignment3 + assignment4) / 4) * .75
    exams = ((exam1 + exam2) / 2) * .25
    final_grade = int((assignments + exams) * 100)
    print("Final Grade is", final_grade, "out of 100")

if __name__ == "__main__":
    main()
