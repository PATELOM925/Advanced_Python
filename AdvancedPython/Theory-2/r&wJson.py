import json

def read_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON data in '{filename}'.")
        return None

def write_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Example usage
if __name__ == "__main__":
    # Sample JSON object
    sample_data = {
        "name": "Shreya Patel",
        "age": 21,
        "email": "patel.com"
    }

    # Write JSON data to a file
    filename = "data.json"
    write_json(filename, sample_data)
    print("JSON data written to 'data.json'.")

    # Read JSON data from the file
    read_data = read_json(filename)
    if read_data:
        print("JSON data read from 'data.json':")
        print(read_data)

        # Modify the JSON data
        read_data["age"] = 28
        read_data["city"] = "Scarborough"
        read_data["name"] = "Shreya S Patel"

        # Write the updated JSON data back to the file
        write_json(filename, read_data)
        print("Updated JSON data written back to 'data.json'.")
