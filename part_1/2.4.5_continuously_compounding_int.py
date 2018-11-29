principal = 5000
rate = 0.05
time = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# One important formula in finance and accounting is the
# formula for continually compounding interest. This formula
# takes as input an amount of money invested, an interest
# rate, and an amount of time (in years), and returns the
# value of the investment after that period of time.
#
# The formula is:
#
#   amount = principal * e ^ (rate * time)
#
# Add some code below that will find the amount of money in
# an account with the initial investment, interest rate, and
# number of years given by the variables above. Note,
# however, that we've gone ahead and supplied you the print
# statement: you shouldn't need to change this. Instead, just
# complete this code such that the variable 'amount' is
# created with the right value.
#
# Note that e is a constant; you may access it with math.e --
# you can use math.e as a variable like any other after
# importing math:

import math

# Add your code here such that there exists a variable named
# 'amount' with the amount in the account after the given
# time at the given interest rate.
amount = principal * math.e ** (rate * time)

# Don't touch the line of code below!
print("After " + str(time) + " years invested with a " + str(rate) + " interest rate, a $" + str(
    principal) + " investment will be worth $" + str(round(amount, 2)) + ".")
