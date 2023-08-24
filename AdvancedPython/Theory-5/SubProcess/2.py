import subprocess

def pipeline_example():
    try:
        data = "Hello, Students! \n How \n are you?"
        print("Ouput before filtering\n",data)
        echo_process = subprocess.Popen(['echo', data], stdout=subprocess.PIPE)
        #this filtering works using our value, and our value must be the first word of a line ( \n --> before it)
        grep_process = subprocess.Popen(['grep', 'are'], stdin=echo_process.stdout, stdout=subprocess.PIPE)
        echo_process.stdout.close()
        output = grep_process.communicate()[0].decode('utf-8')
        print("Output after filtering:")
        print(output)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    pipeline_example()
