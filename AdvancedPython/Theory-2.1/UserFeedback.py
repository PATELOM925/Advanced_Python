import json

def submit_feedback():
    print("Submit your feedback:")
    name = input("Enter your name (optional): ")
    feedback = input("Enter your feedback: ")
    PhoneNo = int(input("Enter Your Phone no: "))

    with open("feedback.txt", mode="a") as file:
        detils = {"name": name, "feedback": feedback,"Phone Number": PhoneNo}
        json.dump(detils, file)
        file.write("\n")

    print(f"Thank you for your valuable feedback, {name if name else 'valued customer'}!")

def main():
    while True:
        print("\n1. Submit Feedback")
        print("2. Exit")
        choice = input("Enter your choice (1  or  2): ")

        if choice == "1":
            submit_feedback()
        elif choice == "2":
            print("Thanks")
            break
        else:
            print("Invalid choice. Please try again.")

main()