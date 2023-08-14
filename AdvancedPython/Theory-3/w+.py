def writeplus(filename):
    filename = "text.txt"
    with open(filename, 'w+') as f:
        data = f.read()
        f.seek(0)
        print("reading the file")
    return data

def write(filename):
    with open(filename,'w+') as f:
        data = f.read()
        i = input("Write your file: ")
        f.write(i)
        print("Written in the file")
    return data

def main():
    print("\n1. Read with w+")
    print("\n2. Write in the file")
    choice = input("Enter your choice (1  or  2): ")

    if choice == "1":
        writeplus("file.txt")
    elif choice =="2":
        write("file.txt")    
    else:
        print("Invalid choice. Please try again.")
main()        
        