# In the previous coding problem, you created a function
# called hide_and_seek that printed the numbers from 1 to 10.
# Now, however, we want to extend that. What if we want to
# count to 20? 30?
#
# Modify your previous function so that it takes as input one
# parameter: count. Then, instead of printing the numbers from
# 1 to 10, it should print the numbers from 1 to the value of
# count. Then, end with "Ready or not, here I come!"


# Write your function here!
def hide_and_seek(count):
    for i in range(1, count + 1):
        print(i)
    print("Ready or not, here I come!")


# The function call below will test your function. We'll delete
# and overwrite this with other calls to hide_and_seek with
# different numbers during grading:
hide_and_seek(36)
