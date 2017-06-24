# Gather user info for standard input
print ("How old are you?", end="")
age = input()
print ("How tall are you?", end="")
height = input()
print ("How much do you weigh?", end="")
weight = input()

# Print raw to see example ' and " in height
print ("So, you're %r old, %r tall, and %r heavy." % 
       (age, height, weight))