# get_line returns the number of characters on specific line number in a file

def get_line(filename, line_number):
  # Open the file in read mode
  with open(filename, 'r') as f:
    # Read the lines of the file into a list
    lines = f.readlines()
    # Check if the specified line number is out of range
    if line_number > len(lines):
      # Print an error message if the line number is out of range
      print(f'Error: Line number {line_number} does not exist')
      return
    # Return the length of the specified line
    return len(lines[line_number - 1])
