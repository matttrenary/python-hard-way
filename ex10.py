# Testing out some escaped characters
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

# See how it works within a triple
fat_cat = ("""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""")

print (tabby_cat)
print (persian_cat)
print (backlash_cat)
print (fat_cat)

# Others that are helpful
# \r - return to start of line. Prob want \n
# \f - new page/section essentially
# \v - vert tab