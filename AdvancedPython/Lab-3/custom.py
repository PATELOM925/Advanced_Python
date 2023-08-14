class OSNotFoundException(Exception):
    pass

class OSNotSupportedException(Exception):
    pass

class OSVersionNotSupportedException(Exception):
    pass

class PythonVersionNotFoundException(Exception):
    pass

class LibsNotFoundException(Exception):
    pass

class LibsVersionNotMentionedException(Exception):
    pass

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def validate_input_data(input_data):
    requirements = {}
    libs = {}

    for line in input_data:
        key, value = line.split(':')
        key = key.strip()
        value = value.strip()
        
        if key == 'OS':
            requirements[key] = value
        elif key == 'OS_VERSION':
            requirements[key] = value
        elif key == 'Python':
            requirements[key] = value
        elif key == 'numpy':
            libs[key] = value
        elif key == 'pandas':
            libs[key] = value
        elif key == 'tensorflow':
            libs[key] = value
        else:
            raise LibsNotFoundException(f"Invalid library: {key}")

    validate_os(requirements)
    validate_libs(libs)

    return requirements, libs

def validate_os(requirements):
    supported_os = ['Ubuntu', 'Mac', 'Windows']  # Add more supported OS
    if 'OS' not in requirements:
        raise OSNotFoundException("OS not found")
    elif requirements['OS'] not in supported_os:
        raise OSNotSupportedException("OS not supported")

    # Add your OS version validation logic here
    os_version = requirements.get('OS_VERSION')
    if os_version and not validate_os_version(os_version):
        raise OSVersionNotSupportedException(f"OS version '{os_version}' not supported")

def validate_os_version(os_version):
    supported_versions = ["18.02", "18.04", "20.04"]  # Add supported versions
    return os_version in supported_versions

def validate_libs(libs):
    supported_libs = ['numpy', 'pandas', 'tensorflow']  # Add more supported libs
    for lib in libs:
        if lib not in supported_libs:
            raise LibsNotFoundException(f"Library '{lib}' not found")

def generate_output(requirements, libs):
    output = "System Requirements:\n"
    output += f"OS: {requirements['OS']} {requirements['OS_VERSION']}\n"
    output += f"Python Version: {requirements.get('Python', 'Not specified')}\n"
    output += "Libraries:\n"
    for lib, version in libs.items():
        output += f" - {lib}: {version}\n"
    return output

def main():
    input_data = read_input_file('req.txt')
    
    try:
        requirements, libs = validate_input_data(input_data)
    except (OSNotFoundException, OSNotSupportedException, 
            OSVersionNotSupportedException, PythonVersionNotFoundException,
            LibsNotFoundException, LibsVersionNotMentionedException) as e:
        print(f"Validation failed: {str(e)}")
        return
    
    output_content = generate_output(requirements, libs)
    
    with open('output.txt', 'w') as output_file:
        output_file.write(output_content)
    
    print("Output file 'output.txt' generated successfully.")

if __name__ == '__main__':
    main()
