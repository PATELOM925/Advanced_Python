def readplus(filepath):
    with open(filepath, 'r+') as f:
        data = f.read()
        print("reading the file")
        print(data)
    return data

def readwrite(filename):
    with open(filename,'r+') as f:
        data = f.read()
        i = input("Write your file: ")
        f.write(i)
        print("Written in the file")
    return data    
        
def main():
        print("\n1. read with r+")
        print("2. write with r+")
        choice = input("Enter your choice (1  or  2): ")

        if choice == "1":
            readplus("text.txt")
        elif choice == "2":
            readwrite("text.txt")
            
        else:
            print("Invalid choice. Please try again.")

main()     