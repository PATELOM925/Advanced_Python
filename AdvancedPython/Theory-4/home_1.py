import zlib

def compress_data(input_data):
    compressed_data = zlib.compress(input_data, level=zlib.Z_BEST_COMPRESSION)
    return compressed_data

def decompress_data(compressed_data):
    decompressed_data = zlib.decompress(compressed_data)
    return decompressed_data

# Example data
input_text = "text that we want to compress using zlib." * 1000

# Compress the data
compressed_data = compress_data(input_text.encode('utf-8'))
print("Compressed data length:", len(compressed_data))

# Decompress the data
decompressed_text = decompress_data(compressed_data).decode('utf-8')
print("Decompressed text:", decompressed_text[:200]) 
# Prints the first 200 char