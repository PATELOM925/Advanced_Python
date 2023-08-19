import zlib
import zipfile

# Data compression

data = "This is a sample data string containing repetitive text."

# Compress the data string using UTF-8 encoding and the zlib.compress() function
compressed_data = zlib.compress(data.encode("utf-8"))

# Print the original size of the data
print("Original size of data:", len(data))

# Print the size of the compressed data
print("Size of compressed data:", len(compressed_data))

# Decompress the compressed data using the zlib.decompress() function
decompressed_data = zlib.decompress(compressed_data)

# Print the size of the decompressed data
print("Size of decompressed data:", len(decompressed_data))

# Validate whether the decompressed data matches the original data
if data == decompressed_data.decode("utf-8"):
    print("Data decompression is successful.")
else:
    print("Data decompression is unsuccessful.")

# File compression and archiving

# Create a ZIP archive named "parth.zip"
with zipfile.ZipFile("parth.zip", "w") as zip_file:
    zip_file.write("app.pdf", compress_type=zipfile.ZIP_DEFLATED)

# Print a message indicating that the file has been successfully zipped
print("File 'app.pdf' has been successfully zipped.")

# File extraction

# Open the "parth.zip" archive using the ZipFile class and the with statement
with zipfile.ZipFile("parth.zip", "r") as zip_file:
    # Extract all contents of the archive to a directory named "Extract"
    zip_file.extractall("Extract")

# Print a message indicating that the files have been successfully extracted
print("Files from 'parth.zip' have been successfully extracted to 'Extract' directory.")
