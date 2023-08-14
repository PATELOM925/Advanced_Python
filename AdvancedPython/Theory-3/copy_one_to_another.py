import os
import shutil

def copy_file(source_dir,destination_dir):
    
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg"):
            source_file = os.path.join(source_dir,filename)
            destination_file = os.path.join(destination_dir,filename)
            shutil.copy(source_file,destination_file)
            print("File copied: " , source_file , "to" , destination_dir)
            
def main():
    destination_dir = "destination" #naming our directory
    os.makedirs(destination_dir) #creating new directory using os 
    print("Destination , a new directory created",destination_dir)
    source_dir = "source"
    copy_file(source_dir,destination_dir)
    
    #navigate in directory
    current_dir  = os.getcwd() #getting current working directory
    print("Current working directory is: ",current_dir)
    
    parent_dir = os.path.dirname(current_dir) #getting parent directory
    print("PArent directory is: ",parent_dir)
    
    child_dir = [d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir))]
    print("Child directories: ",child_dir)
    
    
main()            