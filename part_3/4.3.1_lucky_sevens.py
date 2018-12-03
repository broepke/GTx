# Write a function, called lucky_sevens, that takes in one
# parameter, a list of integers, and returns True if the list
# has three '7's  in a row and False if the list doesn't.
#
# For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
# Hint: As soon as you find one instance of three sevens, you
# could go ahead and return True -- you only have to find it
# once for it to be True! Then, if you get to the end of the
# function and haven't returned True yet, then you might
# want to return False.


# Write your function here!
def lucky_sevens(a_list):
    seven_counter = 0
    was_a_seven = False

    for i in a_list:
        if i == 7:
            seven_counter += 1
            was_a_seven = True
            if seven_counter == 3:
                return True
        else:
            was_a_seven = False
            seven_counter = 0

    return False


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))
