# Demonstrate various file and directory operations with os and shutil modules: 
# create, delete, move, copy, list all files in the directory/subdirectories

import os  # Import the os module to work with directories and files
import shutil  # Import the shutil module to perform file operations

# Function to create a directory
def create_directory(dir_name):
    try:
        os.mkdir(dir_name)  # Create the directory with the specified 'dir_name'
        print(f"Directory '{dir_name}' created successfully!")  # Print a success message
    except FileExistsError:  # If the directory already exists, catch the exception
        print(f"Directory '{dir_name}' already exists.")

# Function to delete a directory , for deleting we use rmtree technique
def delete_directory(dir_name):
    try:
        shutil.rmtree(dir_name)  # Delete the entire directory tree with the specified 'dir_name'
        print(f"Directory '{dir_name}' deleted successfully!")  # Print a success message
    except FileNotFoundError:  # If the directory is not found, catch the exception
        print(f"Directory '{dir_name}' not found.")
    except OSError as e:  # If any other error occurs while deleting, catch the OSError
        print(f"Error occurred while deleting '{dir_name}': {e}")

# Function to move a file or directory to a new location (move means cut & paste)
def move_file_or_directory(src, dest):
    try:
        shutil.move(src, dest)  # Move the 'src' file or directory to the 'dest' location
        print(f"Moved '{src}' to '{dest}' successfully!")  # Print a success message
    except FileNotFoundError:  # If the 'src' or 'dest' is not found, catch the exception
        print(f"File or directory '{src}' not found.")
    except shutil.Error as e:  # If any other error occurs while moving, catch the shutil.Error
        print(f"Error occurred while moving '{src}' to '{dest}': {e}")

# Function to copy a file or directory to a new location (copy & paste)
def copy_file_or_directory(src, dest): 
    if os.path.exists(src):  # Check if the source file or directory exists
        try:
            shutil.copy(src, dest)  # Copy the 'src' file or directory to the 'dest' location
            print(f"Copied '{src}' to '{dest}' successfully!")  # Print a success message
        except FileNotFoundError:  # If the 'src' or 'dest' is not found, catch the exception
            print(f"File or directory '{src}' not found.")
        except shutil.Error as e:  # If any other error occurs while copying, catch the shutil.Error
            print(f"Error occurred while copying '{src}' to '{dest}': {e}")
    else:
        print(f"Source file or directory '{src}' not found.")  # Print an error message if the source doesn't exist

# Function to navigate the file system and list files in a directory
def list_files_in_directory(dir_name):
    try:
        print(f"Files in directory '{dir_name}':")  # Print the directory name
        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(dir_name):  
            for file in files:  # Iterate through the files in the current directory
                print(os.path.join(root, file))  # Print the path of each file
    except FileNotFoundError:  # If the directory is not found, catch the exception
        print(f"Directory '{dir_name}' not found.")
# os.walk(directory_path) generates a tuple of three values for each directory visited in the directory tree: 
# root: The current directory path.
# dirs: A list of directory names within the current directory.
# files: A list of file names within the current directory.
# Example usage
directory_name = "Example_Directory"  # Set the name of the directory to be used in the examples
create_directory(directory_name)  # Call the function to create a directory

#create two files in the directory: example.txt and example_copy.txt
file_to_move = "example.txt"  # Set the name of the file to be moved
file_to_copy = "example_copy.txt"  # Set the name of the file to be copied

move_file_or_directory(file_to_move, directory_name)  # Call the function to move a file
copy_file_or_directory(file_to_copy, directory_name)  # Call the function to copy a file

list_files_in_directory(os.path.dirname(os.getcwd()))  # Call the function to list files in the directory

#delete_directory(directory_name)  # Call the function to delete the directory
