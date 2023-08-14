def display_quiz_questions(filename):
    # Open the file "quiz.txt" in read mode and create a file object named "file".
    with open("quiz.txt", "r") as file:
        # Initialize variables for storing the question and option.
        question = ""
        option = ""

        # Loop through each line in the file.
        for line in file:
            # Remove any leading or trailing white spaces from the line.
            line = line.strip()

            # Check if the line ends with a question mark ("?"), indicating it's a question.
            if line.endswith("?"):
                # If there is already a question and option, display the previous question and option.
                if question:
                    print(question)
                    print(option)

                # Assign the current line to the 'question' variable.
                question = line
                # Reset the 'option' variable to an empty string for the new question.
                option = ""
            else:
                # If the line doesn't end with a question mark, it's an option for the current question.
                # Append the line to the 'option' variable.
                option += line

        # After the loop ends, display the last question and option found in the file.
        print(question)
        print(option)

filename = "quiz.txt"  # Replace "quiz.txt" with the name of your quiz file
display_quiz_questions(filename)
