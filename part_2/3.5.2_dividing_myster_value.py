mystery_value = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a program that divides mystery_value by mystery_value
# and prints the result. If that operation results in an
# error, divide mystery_value by (mystery_value + 5) and then
# print the result. If that still fails, multiply mystery_value
# by 5 and print the result. You may assume one of those three
# things will work.
#
# You may not use any conditionals.
#
# Hint: You're going to want to test one try/except structure
# inside another! Think carefully about whether the second
# one should go inside the try block or the except block.


# Add your code here!


try:
    print(mystery_value / mystery_value)
except:
    try:
        print(mystery_value / (mystery_value + 5))
    except:
        print(mystery_value * 5)
