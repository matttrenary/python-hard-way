# Gather user info from standard input
# Lot simpler this way than ex11.py
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

# Print raw to see example ' and " in height
print ("So, you're %r old, %r tall, and %r heavy." % 
       (age, height, weight))