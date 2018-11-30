# Write a function called "steps" that should return a string
# that, if printed, looks like this:
#
# 111
#	222
#		333
#
# Note that the characters at the beginning of the second and
# third lines must be tabs, not spaces. There should be one
# tab on the second line and two on the third line.
#
# You may only declare ONE string in your function.
#
# Hint: Don't overthink this! We're literally just asking you
# to return one single string that just holds the above text.
# You don't have to build the string dynamically or anything.


# Write your function here!
def steps():

    my_string = "111\n\t222\n\t\t333"

    return my_string

# The line below will test your function.
print(steps())




