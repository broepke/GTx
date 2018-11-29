principal = 5000
rate = 0.05
time = 5
goal = 7000

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Recall in problem 2.4.5 you wrote some code that calculated
# the amount of money in an account based on this formula:
#
#   amount = principal * e ^ (rate * time)
#
# Those three variables are given above again, as well as a
# fourth: goal. We want to see if the investment given by
# these values will exceed the goal. If it will, we want to
# print this message:
#
#  "You'll exceed your goal by [extra money]"
#
# If it will not, we want to print this message:
#
#  "You'll fall short of your goal by [needed money]"
#
# If the investor will meet their goal, [extra money] should
# be the final amount minus the goal. If the investor will
# not meet their goal, [needed money] will be the goal minus
# the final amount.
#
# To make the output more legible, though, we want to round
# the difference to two decimal places. If the difference is
# contained in a variable called 'difference', then we can
# do this to round it: rounded_diff = round(difference, 2)
#
# Working with new and unfamiliar functions or abilities is
# part of learning to code, so use this function in your
# answer!

import math

# Remember, you can access e with math.e.


# Add your code here! Feel free to copy your code from
# problem 2.4.5.

success = False
delta = 0.00
amount = principal * math.e ** (rate * time)
line = "Foo"

if goal < amount:
    success = True
    delta = amount - goal
    line = "You'll exceed your goal by "
else:
    delta = goal - amount
    line = "You'll fall short of your goal by "

delta = round(delta, 2)

print(line + str(delta))
