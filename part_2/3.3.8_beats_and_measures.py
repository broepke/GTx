beats_per_measure = 4
measures = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Recall our earlier problem where you printed out beats based
# on measures and beats per measure (3.3.5 Coding Exercise 1).
# In that exercise, you printing out 1 through the number of beats
# in a measure over and over depending on the number of measures.
#
# Copy and modify your code, but this time, you should replace the
# number 1 with the number of the current measure. So, the first
# number in each measure will always rise.
#
# For example, instead of 1 2 3 4 1 2 3 4 1 2 3 4 (with each
# number on its own line), you'd now print 1 2 3 4 2 2 3 4 3 2 3 4,
# and so on.
#
# You can use our sample answer from that problem if you'd prefer.
#
# HINT: One approach would involve adding a conditional.


# Add your code here! Using the original values of the variables
# above, this will initially print the following numbers (but each
# on their own line):
# 1 2 3 4 2 2 3 4 3 2 3 4 4 2 3 4 5 2 3 4

loop_counter = 0

for i in range(1, measures + 1):
    loop_counter = i
    for i in range(1, beats_per_measure + 1):
        if i == 1:
            print(loop_counter)
        else:
            print(i)
