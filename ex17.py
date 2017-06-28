from sys import argv
from os.path import exists

# Read in old and new file names
script, from_file, to_file = argv

# Let the user know what's happening
print("Copying from {} to {}".format(from_file, to_file))

indata = open(from_file).read()

# Spit back size of file
print("The input tile is {} bytes long".format(len(indata)))

# Check and confirm for new file overwrite
print("Does the output file exist? {}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w').write(indata)

print("Alright, all done.")
