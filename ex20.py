# Read a file and print some things from it
from sys import argv

script, input_file = argv

# Our functions to manipulate a file
def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
# Gotta get our file eh
current_file = open(input_file)

# Whole file - there are easier ways
print("First let's print the whole file:\n")

print_all(current_file)

# Head back to start - again there are easier ways
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

# Print some lines - pretty inefficient
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)