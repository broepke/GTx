cold = False
windy = False

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In this problem, we want to print the message, "You should
# wear a jacket today!" if it's cold or windy, or the message
# "You don't need a jacket today!" if it's not.
#
# At the bottom of this file, we've added some code that
# handles printing these two messages. For this code to work,
# the variable need_jacket needs to exist. Its value should be
# True (the boolean, not the string) if it's cold or windy,
# False if it's neither cold nor windy.


# Add your code to create the variable need_jacket with the
# appropriate value here!
need_jacket = (cold or windy)

# Do not modify the code below. It will work if you have
# correctly create the variable need_jacket with the
# appropriate value.
if need_jacket:
    print("You should wear a jacket today!")
else:
    print("You don't need a jacket today!")
