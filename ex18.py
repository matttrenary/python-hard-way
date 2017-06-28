# First script with functions
# This is like our script with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
# OK that *args is actually pointless
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
# This one just takes one argument
def print_one(arg1):
    print("arg1: {}".format(arg1))
    
# Don't need arguments
def print_none():
    print("I got nothin'.")

# Run the functions
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()