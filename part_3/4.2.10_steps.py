# Now, let's improve our steps() function to take one parameter
# that represents the number of 'steps' to print. It should
# then return a string that, when printed, shows output like
# the following:
#
# print(steps(3))
# 111
#	222
#		333
#
# print(steps(6))
# 111
#	222
#		333
#			444
#				555
#					666
#
# Specifically, it should start with 1, and show three of each
# number from 1 to the inputted value, each on a separate
# line. The first line should have no tabs in front, but each
# subsequent line should have one more tab than the line
# before it. You may assume that we will not call steps() with
# a value greater than 9.
#
# Hint: You'll want to use a loop, and you'll want to create
# the string you're building before the loop starts, then add
# to it with every iteration.


# Write your function here!
def steps(num):
    i = 1
    a_string = ""

    while i <= num:
        a_string += str(i) * 3 + "\n" + ("\t" * i)

        i += 1

    return a_string

# The following two lines will test your code, but are not
# required for grading, so feel free to modify them.
print(steps(3))
print(steps(6))
