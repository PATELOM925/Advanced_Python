class CustomError(Exception):
    """A custom exception class."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def custom_function(value):
    if value < 0:
        raise CustomError("Value cannot be negative")

try:
    user_input = int(input("Enter a number: "))
    custom_function(user_input)
except CustomError as e:
    print(f"CustomError: {e}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
