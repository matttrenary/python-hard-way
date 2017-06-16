# Our output string that is just 4 variables
formatter = "%r %r %r %r"

# Printing out 4 numbers, r will take whatever
print (formatter % (1, 2, 3, 4))
# Printing out 4 strings
print (formatter % ("one", "two", "three", "four"))
# Printing out 4 booleans
print (formatter % (True, False, False, True))
# Printing 4x our format string.
# Just considering % as a %
print (formatter % (formatter, formatter, formatter, formatter))
# Print four more strings but we can list them on
# ...mult lines because they are in parens
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))