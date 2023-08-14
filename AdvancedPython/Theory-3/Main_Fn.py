import test
print("I am in Main_Fn file")
test.my_fun()
if __name__ == "__main__":
              print("Main_Fn.py will run as standalone")
else:
              print("Main_Fn.py will run only when imported")
# The main function is mandatory in programs like C, Java, etc, but it is not necessary for python to 
# use the main function. However it is a good practice to use it.
# A Python programme uses the condition if __name__ == '__main__' to only run the code inside the 
# if statement when the program is run directly by the Python interpreter. 
# The code inside the if statement is not executed when the file's code is imported as a module.