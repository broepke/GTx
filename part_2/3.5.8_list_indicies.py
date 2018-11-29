a_list = [1, 2, 3, 4, 5]
list_index = 7

# -----------------------------------------------------------
# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In this problem, we're going to use some unfamiliar syntax.
# You'll learn more about this syntax in Unit 4. For now,
# though, you don't need to understand the syntax. All you
# need to know is that right now, this code will cause an
# error with the values supplied above.
#
# Revise this code so that this error is caught, and the
# message "Invalid index!!" is printed. However, your revision
# must meet these requirements, too:
#
# - If the values of the variables above are changed so
#   that the error doesn't occur, the program should behave
#   the same way that it does now.
# - The two first and last lines, "Accessing index..." and
#   "Done!", should print whether or not an error occurs.
# - If a *different* error occurs from the one that arises
#   initially, your code should instead print "Unknown
#   error!"
#
# HINT: You won't be able to do this without running the code
# first and seeing what the error is. So, try it out first!

# Revise this code:


print("Accessing index...")
try:

    result = a_list[list_index]
    print("Value at index:", result)

except IndexError:
    print("Invalid index!!")

except:
    print("Unknown error!")

print("Done!")
