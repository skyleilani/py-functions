# summarize_file takes a file to summarize and returns the total number of characters and lines in a file. 

def summarize_file(filename):
  
  # handle error if filename isnt a string
  if type(filename) != str: 
    print('Error: filename must be in string format')
    return 
  
  # initialize variables to track the total number of characters and lines
  total_characters = 0
  line_count = 0
  
  # open file in read mode
  with open(filename, 'r') as f:
    # iterate over lines in the file
    for line in f:
      # add the length of the current line to the total character count
      total_characters += len(line)
      # increase the line count by 1
      line_count += 1
      
  # Print the total number of characters and lines in the file
  print(f'Total characters: {total_characters}')
  print(f'Total lines: {line_count}')\
  
  
  
  
  
