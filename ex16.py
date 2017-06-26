from sys import argv

script, filename = argv

# Give them a chance to opt out for typo, etc.
print("We're going to erase {}.".format(filename))
print("If you don't want that hit CTRL-C (^C).")
print("If you do what that, hit RETURN.")

# Prompt for the return (or anything)
input("?")

print("Opening the file...")
target = open(filename, 'w')

# Do we need to truncate if w? Don't think so
print("Truncating the file. Goodbye!")
target.truncate()

# Get our lines
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Put them in file
print("I'm going to write these to the file.")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("And finally, we close it.")
target.close()