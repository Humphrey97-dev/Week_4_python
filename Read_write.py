# Function to read a file, modify content, and write to a new file
def read_and_modify_file(input_file, output_file):
    try:
        # Openning the input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modifying the content
        modified_content = content.replace("Hello", "Hi")
        
        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# how to use
input_file = "example.txt"
output_file = "modified_example.txt"
read_and_modify_file(input_file, output_file)
