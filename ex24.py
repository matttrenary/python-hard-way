# Longer script
# Some printing with escapes
print("Let's practice everything")
print('You\'d need to know \'bout escapes \\ that do:')
print('\n newlines and \t tabs.')

# Print with the triple
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs to love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")

# Some formatting and messing around with a function
# and some integer/float stuff
five = 10 - 2 + 3 - 6
print("This should be five: {}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# It's just like with an f string
# Which I can't do in 3.5 so whatever
print("We'd have {} beans , {} jars, and {} crates.".format(beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# This is an easy way to apply a list to a format string
print("We'd have {} beans , {} jars, and {} crates.".format(*formula))