# Demonstrate various file and directory operations with os and shutil modules: 
# create, delete, move, copy, list all files in the directory/subdirectories

import os
import shutil

#create ddirectory
def create_dir(name):
    try:
        os.mkdir(name)
        print(f"Directory: {name} created successfully")
    except FileExistsError:
        print(f"Directory: {name} already exists")
        
#deleting directory using rmtree        
def delete_dir(name):
    try:
        shutil.rmtree(name)
        print(f"Directory: {name} deleted successfully")
    except FileNotFoundError:
        print(f"Directory: {name} not found")
    except OSError as e:
        print(f"Error occurred while deleting {name}: {e}")
      
#moving file/directory        
def move_dir(src,dest):
    try:
        shutil.move(src,dest)
        print(f"Moved {src} to {dest} successfully")
    except FileNotFoundError:
        print(f"File/destination doesnt exists at {src}")  
    except shutil.Error as s:
        print(f"Error occured in copying {src} to {dest}: {s}")    
        
#copying file/directory
def copy_dir(src,dest):
    if os.path.exists(src):  #checking if our file exists at src 
        try:
            shutil.copy(src,dest)
            print(f"Copied {src} to {dest} successfully")
        except FileNotFoundError:
            print(f"File/destination doesnt exists at {src}")  
        except shutil.Error as s:
            print(f"Error occured in copying {src} to {dest}: {s}")    
    else:
        print(f"Source file or directory '{src}' not found.")          
        
def list_files_in_dir(name):
    try:
        print(f"files is directory: {name} are ")        
        for root,dir,files in os.walk(name):
            for file in files:
                print(os.path.join(root,file))
    except FileNotFoundError:
        print(f"Directory {name} not Found ")      
        
def main():
    print("1. Create Directory")
    print("2. Delete Directory")
    print("3. Move Directory")
    print("4. Copy Directory")
    print("5. List Files in Directory")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter directory name: ")
        create_dir(name)
    elif choice == "2":
        name = input("Enter directory name: ")
        delete_dir(name)
    elif choice == "3":
        src = input("Enter source directory: ")
        dest = input("Enter destination directory: ")
        move_dir(src,dest)
    elif choice == "4":
        src = input("Enter source directory: ")
        dest = input("Enter destination directory: ")
        copy_dir(src,dest)
    elif choice == "5":
        name = input("Enter directory name: ")
        list_files_in_dir(name)
    else:
        print("Invalid choice. Please try again.")
main()              
                    