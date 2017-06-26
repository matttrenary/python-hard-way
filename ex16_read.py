from sys import argv

script, filename = argv

print("The contents of your file {}:".format(filename))

target = open(filename)
print(target.read())