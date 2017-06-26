# First import - argument variable
from sys import argv
script, first, second, third = argv

# Just spitting them back
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Extra credit - get input back based on what is passed in argv
response = input("What are your thoughts about {}? ".format(first))
print(response)