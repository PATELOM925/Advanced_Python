import os 

class CustomFileOpenError(Exception):
    """Custom exception for file open errors."""
    pass

class CustomFileReadError(Exception):
    """Custom exception for file read errors."""
    pass

class CustomFileWriteError(Exception):
    """Custom exception for file write errors."""
    pass

def open_binary_file(file_path, mode):
    try:
        file_handle = open(file_path, mode)
    except OSError as e:
        raise CustomFileOpenError(f"Error opening file '{file_path}': {e}")
    
    return file_handle

def read_binary_data(file_handle, num_bytes):
    try:
        data = file_handle.read(num_bytes)
        if not data:
            raise CustomFileReadError("Error reading data from file.")
        return data
    except Exception as e:
        raise CustomFileReadError(f"Error reading data from file: {e}")

def write_binary_data(file_handle, data):
    try:
        file_handle.write(data)
    except Exception as e:
        raise CustomFileWriteError(f"Error writing data to file: {e}")

if __name__ == "_main_":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    try:
        file_path = os.path.join(current_directory, "binary_file.bin")
        file_handle = open_binary_file(file_path, "rb")

        try:
            data = read_binary_data(file_handle, 1024)
            print("Read data:", data)
        except CustomFileReadError as e:
            print(e)
        finally:
            if file_handle:
                file_handle.close()  # Close the file handle in the finally block
    except CustomFileOpenError as e:
        print(e)