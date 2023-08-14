def calculate_grade(marks):
    if marks >= 80:
        print("Excellent Grade (O)")
    elif marks >= 70:
        print("Outstanding Grade (A+)")
    elif marks >= 60:
        print("Very Good Grade (A)")
    elif marks >= 50:
        print("Good Grade (B+)")
    elif marks >= 40:
        print("Satisfactory Grade (B)")
    elif marks >= 30:
        print("Acceptable Grade (C)")
    elif marks >= 20:
        print("Needs Improvement Grade (D)")
    else:
        print("Poor Grade (F)")

def check_pass_fail(marks):
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

def main():
    total_subjects = int(input("Enter the total number of subjects: "))

    for i in range(1, total_subjects + 1):
        print(f"Enter the marks of subject {i}:")
        marks = int(input())
        calculate_grade(marks)
        check_pass_fail(marks)
        print()

main()
