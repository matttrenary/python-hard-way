# String formatting for an int
x = "There are %d types of people." % 10

# String formatting with strings
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing the string formats above to tell the joke
print (x)
print (y)

# Repeat for those who missed it
# r will display x in quotes. Raw representation?
print ("I said: %r." % x)
# Or you can just put the quotes in yourself with a string
print ("I also said: '%s'." % y)

# Can piece together the formatting separately
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

# Easy to combine strings, just +
w = "This is the left side of..."
e = "a string with a right side."

print (w + e)