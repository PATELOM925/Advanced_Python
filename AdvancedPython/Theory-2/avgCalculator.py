def avg_grade(filename):
    total_grades = 0
    num_students = 0

    with open(filename, "r") as file:
        for line in file:
            student_info = line.strip().split(",")
            if len(student_info) == 2:
                grade = float(student_info[1])
                total_grades += grade
                num_students += 1

    if num_students > 0:
        average_grade = total_grades / num_students
        return average_grade
    else:
        return None

filename = "grades.csv"
average_grade = avg_grade(filename)

if average_grade is not None:
    print(f"The average grade of the students is: {average_grade:.2f}")
else:
    print("No student data found in the file.")
