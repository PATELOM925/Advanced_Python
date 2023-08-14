#perform didfferent file operations

import os
import shutil
import time
import stat
import random

def main():
    filename = "name_change.txt"
    filename2 = "complex.txt"
    
    # #writing data to a file
    # write_file(filename)
    # print("_____")
    
    # #reading data from a file
    # read_file(filename)
    # print("_____")
    
    # #reading a line from file
    # read_line(filename)
    # print("_____")

    # #reading all line from file , (returns of list of lines one by one)
    # read_all_line(filename)
    # print("_____")
    
    # #writing list of strings
    # write_list(filename)
    # print("_____")
    
    # #move file pointe and get current position
    # move_file_pointer(filename)
    # print("_____")
    
    # #flushing the file buffer
    # flush_fileBuffer(filename)
    # print("______")
    
    # #closing the file explicityyl
    # close_file(filename)
    # print("______")
    
    # #renaming the file
    # rename_file("complex.txt","name_change.txt")
    # print("______")
    
    #deleting file
    #delete(filename)
    #print("______")
    
    # #getting and changing file permissions
    # get_set_file_permission(filename)
    # print("_____")
    
    # #getting metadata
    # get_metadata(filename)
    # print("_____")
    
    
def write_file(filename):
    with open(filename,"w") as f:
        data_to_write = "SAMPLE DATA"
        f.write(data_to_write)
        print("Data written to file")
        
def read_file(filename):
    with open(filename,"r") as f:
        data = f.read()
        print("Data  from file is : ",data) 
        print(data)
 
def read_line(filename):
    with open(filename,"r") as f:
        data = f.readline()
        print("Data  from file is : ",data) 
        print(data)
        
def read_all_line(filename):
    with open(filename,"r") as f:
        data = f.readlines() #returns list where each element of string is a single line of the file
        print("Data  from file is : ",data) 
        print(data)
        
def write_list(filename):
    with open(filename,"w") as f:
        data_to_write = ["SAMPLE DATA","SAMPLE DATA 2","SAMPLE DATA 3"]
        f.writelines(data_to_write)
        print("Data written to file")
        
def move_file_pointer(filename):
    with open(filename,"r") as f:
        print("Current position of te file poiter is: ",f.tell())
        f.seek(5) #moves the file pointer to 5th position
        print("Moved the file pointer to 5th position")
        print("current position of the file pointer: ",f.tell())
        data = f.read()
        print("Data  from file is : ",data) 
        print(data)  
        
def flush_fileBuffer(filename):
    with open(filename,"w") as f:
        data_to_write = "SAMPLE NEWWWWW DATA"
        f.write(data_to_write)
        print("Data written to file")
        f.flush()
        print("Flushed the file buffer")                                       
    
def close_file(filename):
    with open(filename,"w") as f:
        data_to_write = "FILE CLOSED"
        print("File is open")
        f.write(data_to_write)
        print("Data written to file")
        f.close()
        print("File closed")
        #f.write("SAMPLE DATA 2") #this will throw an error as the file is closed    
        
def rename_file(old_name,new_name):
   try:
       os.rename(old_name,new_name)
       print("File renamed")
   except FileNotFoundError:
       print("File not found")
   except FileExistsError:
       print("file with name: ",new_name,"already exists , use another name for renaming")     
       
def  get_set_file_permission(filename):
    #getting file permission
    file_permission = os.stat(filename).st_mode #st represents fiel type and file modde bits
    print("File permission before changing(in octal): ",oct(file_permission)) #oct
    #changing file permission
    os.chmod(filename,stat.S_IRWXU) #gives read,write and execute permission to the user
    print("File permission after changing(in octal): ",oct(file_permission))
    
def get_metadata(filename):
    file_stat = os.stat(filename)
    print("file size: ",file_stat.st_size,"bytes")
    print("file inode number: ",file_stat.st_ino)
    print("file device: ",file_stat.st_dev)
    print("file uid: ",file_stat.st_uid)
    print("file gid: ",file_stat.st_gid)
    print("file permission: ",oct(file_stat.st_mode))
    print("file number of hard links: ",file_stat.st_nlink)
    print("file last access time: ",time.ctime(file_stat.st_atime))
    print("file last modification time: ",time.ctime(file_stat.st_mtime))
    print("file last status change time: ",time.ctime(file_stat.st_ctime))
    
    
if __name__ == "__main__":
    
  main()
  
  
# stat.S_ISGID: set group ID on execution
# stat.S_ENFMT: record locking enforced
# stat.S_ISVTX: save text image after execution
# stat.S_IREAD: read by owner
# stat.S_IWRITE: write by owner
# stat.S_IEXEC: execute by owner
# stat.S_IRWXU: read, write, and execute by owner
# stat.S_IRUSR: read by owner
# stat.S_IWUSR: write by owner
# stat.S_IXUSR: execute by owner
# stat.S_IRWXG: read, write, and execute by group
# stat.S_IRGRP: read by group
# stat.S_IWGRP: write by group
# stat.S_IXGRP: execute by group
# stat.S_IRWXO: read, write, and execute by others
# stat.S_IROTH: read by others
# stat.S_IWOTH: write by others
# stat.S_IXOTH: execute by others
# stat.S_IFMT: bit mask for the file type bit fields
# stat.S_IFDIR: directory
# stat.S_IFCHR: character device
# stat.S_IFBLK: block device
# stat.S_IFREG: regular file
# stat.S_IFIFO: FIFO (named pipe)
# stat.S_IFLNK: symbolic link
# stat.S_IFSOCK: socket
# stat.S_ISUID: set UID bit
# stat.S_ISGID: set-group-ID bit (see below)
# stat.S_ISVTX: sticky bit (see below)
# stat.S_IRWXU: mask for file owner permissions
# stat.S_IRUSR: owner has read permission
# stat.S_IWUSR: owner has write permission
# stat.S_IXUSR: owner has execute permission
# stat.S_IRWXG: mask for group permissions
# stat.S_IRGRP: group has read permission
# stat.S_IWGRP: group has write permission
# stat.S_IXGRP: group has execute permission
# stat.S_IRWXO: mask for permissions for others (not in group)
# stat.S_IROTH: others have read permission
# stat.S_IWOTH: others have write permission
# stat.S_IXOTH: others have execute permission
# stat.S_ENFMT: file locking enforced
