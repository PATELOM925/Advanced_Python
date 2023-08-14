# Design a program that allows users to log their exercise activities and view their exercise logs. 
# The program should provide a user-friendly interface to input exercise details such as date, exercise type, duration, and calories burned. 
# The exercise logs should be stored in a file for future reference.

def exercise():
    print("Log your exercise activity:") 
    date = input("Date (YYYY-MM-DD): ")
    exercise_type = input("Exercise type: ")
    duration = input("Duration (in minutes): ")
    calories_burned = input("Calories burned: ")

    with open("exercise_logs.txt", mode="a") as file:
        file.write(f"{date},{exercise_type},{duration},{calories_burned}\n")

    print("Exercise activity logged successfully!")

def view():
    print("Exercise Logs:")
    with open("exercise_logs.txt", mode="r") as file:
        for line in file:
            date, exercise_type, duration, calories_burned = line.strip().split(",")
            print(f"Date: {date}, Exercise Type: {exercise_type}, Duration: {duration} minutes, Calories Burned: {calories_burned}")

def main():
    while True:
        print("\n1. Log Exercise Activity")
        print("2. View Exercise Logs")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            exercise()
        elif choice == "2":
            view()
        elif choice == "3":
            print("Thanks For Tracking your excersises , Stay Healthy,Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
