"""
Q1) Ceate a command-line interface that allows users to input a command, execute it as a subprocess, 
and display the captured standard output or standard error messages based on whether the subprocess 
execution was successful or not.
"""
import subprocess
# Python program (Parent process) will create subprocess with run() or Popen()
def run_command(command): # takes a parameter command, which represents the command to be executed.
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        # result = subprocess.run("dir", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, text=True)
        # subprocess.run: Executes the provided command as a subprocess. It will return a CompletedProcess object containing information about the subprocess execution
        # stdout=subprocess.PIPE: Redirects the standard output of the subprocess to a pipe, allowing it to be captured.
        # stderr=subprocess.PIPE: Redirects the standard error output of the subprocess to a pipe, allowing it to be captured.
        # shell=True: Tells the subprocess to use the shell for command execution, allowing for more complex command structures (e.g., using pipes and redirection).
        # text=True: Treats the output as text (string) rather than bytes.
        if result.returncode == 0: # return code 0 means the command executed successfully otherwise a failure
            print("Command executed successfully:")
            print(result.stdout)  # Access and print the output from PIPE programmatically  
        else:
            print("Command execution failed:")
            print(result.stderr)  # Access and print the error output from PIPE programmatically 
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    command = input("Enter your command to run (ls for mac): ")  # e.g. For Windows 'dir' for Unix 'ls'
    run_command(command)




"""
#With Popen() instead of run(): we use communicate() with Popen

import subprocess

def run_command(command):
    try:
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        
        # Wait for the subprocess to finish and capture its output and errors
        stdout, stderr = result.communicate()  # need to add communicate() if we use Popen()
        
        if result.returncode == 0:
            print("Command executed successfully:")
            print(stdout)
        else:
            print("Command failed:")
            print(stderr)
    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    run_command('echo hi')
"""