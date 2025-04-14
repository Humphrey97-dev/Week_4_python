# Function to open and read a file with error handling
def read_file_with_error_handling():
    filename = input("Enter the filename: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example
read_file_with_error_handling()
