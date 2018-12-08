# Write a function called "angry_file_finder" that accepts a
# filename as a parameter. The function should open the file,
# read it, and return True if the file contains "!" on every
# line. Otherwise the function should return False.
#
# Hint: there are lots of ways to do this. We'd suggest using
# either the readline() or readlines() methods. readline()
# returns the next line in the file; readlines() returns a
# list of all the lines in the file.


# Write your function here!
def angry_file_finder(file_name):
    my_file = open(file_name, "r")
    has_bang = False

    for lines in my_file:
        if "!" in lines:
            has_bang = True
        else:
            my_file.close()
            return False

    my_file.close()
    return has_bang

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True
print(angry_file_finder("AngryFileFinderInput.txt"))
