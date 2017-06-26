# Same old argument variable module
from sys import argv

# Reading in (our script) and a file from argv
script, filename = argv

# Get our file open
txt = open(filename)

# Spit back the name and the whole file's text
print("Here's your file {}:".format(filename))
print(txt.read())

# Close the file. No explanation yet
txt.close()

# Get the name a different way
print("Type the filename again:")
file_again = input("> ")

# Get our file again (it could be different)
txt_again = open(file_again)

# Spit it all back again
print(txt_again.read())

# Close it
txt_again.close()