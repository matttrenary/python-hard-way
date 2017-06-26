# More argument variable work
from sys import argv

script, user_name, time_start = argv
# Prompt for user input
prompt = ':: '

# Lots of variables and string formatting
print("Hi {} I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few questions.")

# Lets gets some input from the user
print("Do you like me {}?".format(user_name))
likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have {}?".format(user_name))
computer = input(prompt)

# Spit back with the triple to span multilines
print("""
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
You started this at {}.
""".format(likes, lives, computer, time_start))