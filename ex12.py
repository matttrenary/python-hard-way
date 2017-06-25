# Gather user info from standard input
# Lot simpler this way than ex11.py
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

# Print raw to see example ' and " in height
print ("So, you're {} old, {} tall, and {} heavy.".format(
       age, height, weight))

# Trying to make the switch to Python the Hard Way 3
# But it uses 3.6 and I'm not able to get that
# So will try to do some 3.5 things to make it work
# Like the .format above
# If 3.6....
# print (f"So, you're {age} old, {height} tall, and {weight} heavy.")