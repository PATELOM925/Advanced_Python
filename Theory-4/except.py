# Different Exception Scenarios
def handle_exception_scenarios():
    try:
        # ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError:
        print("Handled ZeroDivisionError")

    try:
        # TypeError
        value = "string" + 5  # Incompatible data types
    except TypeError:
        print("Handled TypeError")

    try:
        # ValueError
        num = int("abc")  # Invalid argument value
    except ValueError:
        print("Handled ValueError")

    try:
        # IOError
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except IOError:
        print("Handled IOError")

    try:
        # IndexError
        my_list = [1, 2, 3]
        item = my_list[5]
    except IndexError:
        print("Handled IndexError")

    try:
        # KeyError
        my_dict = {"key": "value"}
        value = my_dict["nonexistent_key"]
    except KeyError:
        print("Handled KeyError")

    try:
        # NameError
        undefined_variable  # Using an undefined variable
    except NameError:
        print("Handled NameError")


# Handling Multiple Exceptions
def handle_multiple_exceptions():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)

        my_list = [1, 2, 3]
        index = int(input("Enter an index: "))
        item = my_list[index]
        print("Item at index:", item)

        my_dict = {"key1": 5, "key2": 8}
        key = input("Enter a key: ")
        value = my_dict[key]
        print("Value for key:", value)

    except (ZeroDivisionError, ValueError, TypeError):
        print("Handled an error related to division, value, or type.")

    except (IndexError, KeyError):
        print("Handled an error related to index or key.")

    except Exception as e:
        print("Handled an unknown error:", e)
    else:
        print("Operation Successfully Completed without Exceptions")
    finally:
        print("Inside the finally block...")

# Custom Exception for File Operations
class FileOperationError(Exception):
    def __init__(self, message):
        self.message = message

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        raise FileOperationError("File not found")
    except PermissionError:
        raise FileOperationError("Permission denied")

if __name__ == "__main__":
    handle_exception_scenarios()

    handle_multiple_exceptions()

    try:
        filename = input("Enter the filename: ")
        read_file(filename)
    except FileOperationError as e:
        print("File operation error:", e.message)
    except Exception as e:
        print("An unknown error occurred:", e)
