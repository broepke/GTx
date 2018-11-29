years = 2
months = 5
days = 24

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Ever been at a loss for what to do for your significant
# other for Valentine's Day? Let's right some code to generate
# a gift recommendation!
#
# The variables above give the length of the relationship in
# number of years, months, and days. Add some code below to
# print a gift recommendation based on these values:
#
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").
# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").
# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").
# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
#
# Note that no matter what, you should only print one gift.


# Add your code here!
if years >= 4:
    print("dog")
elif years >= 1 and years <= 4:
    print("watch")
elif years < 1 and months >= 6:
    print("concert tickets")
elif months > 0 and months < 6 and days >= 0:
    print("candy")
elif months == 0 and days > 1 and days < 31:
    print("candy")
else:
    print("yacht")
