# r
# The r mode opens the file for reading only. The file pointer is placed at the beginning of the file. If the file does not exist, open() raises a FileNotFoundError.

with open("file.txt", "r") as f:
    content = f.read()
# r+
# The r+ mode opens the file for both reading and writing. Important to note that like r, If the file does not exist, open() raises a FileNotFoundError.

with open("file.txt", "r+") as f:
    content = f.read()
    f.write("New content")
# w
# The w mode opens the file for only writing. You can NOT read in this mode. The file pointer is placed at the start of the file. If the file exists, its content is truncated. If the file does not exist, it is created. Be careful to avoid any data loss.

with open("file.txt", "w") as f:
    f.write("New content")
# w+
# The w+ mode opens the file for both writing and reading. Like w, it too will truncate if the the file exists, or create a new one if it doesn’t.

with open("file.txt", "w+") as f:
    f.write("New content")
    f.seek(0)
    content = f.read()
# a
# The a mode opens the file for appending. The file pointer is placed at the end of the file, so new content is added after the existing content. If the file does not exist, it is created.

# Note: The key difference between a and w is that w truncates the existing content of the file, while a appends data to the end of the file without modifying the existing content.

with open("file.txt", "a") as f:
    f.write("Appended content")
# a+
# The a+ mode opens the file for both appending and reading. The file pointer is placed at the end of the file, so new content is added after the existing content. If the file does not exist, it is created.

with open("file.txt", "a+") as f:
    f.write("Appended content")
    f.seek(0)
    content = f.read()
