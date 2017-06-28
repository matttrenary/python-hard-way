# Copying a file to a new location
from sys import argv
from os.path import exists

# Read in old and new file names
script, from_file, to_file = argv

# Let the user know what's happening
print("Copying from {} to {}".format(from_file, to_file))

out_file = open(to_file, 'w').write(open(from_file).read())
