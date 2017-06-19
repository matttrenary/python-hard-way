days = "Mon Tue Wed Thu Fri Sat Sun"
# Will print across multiple lines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Don't need the %s when it's the end of the format
print ("Here are the days: ", days)
print ("Here are the months: ", months)

# Can print across multiple lines using...
# triples instead of newlines
print ("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")