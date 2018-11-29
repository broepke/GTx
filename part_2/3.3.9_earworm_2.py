lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Recall the Earworm problem (3.3.5 Coding Exercise 2). The
# first time, you would still finish printing the entire list
# of lyrics after lines_of_sanity was exceeded.
#
# Revise that code so that you always stop when lines_of_sanity
# is reached. If lines_of_sanity is 6, you would print 6 lines,
# no matter how many lines are in the list. If there are fewer
# than 6 lines in the list, then you'd repeat the list until
# the number of lines is reached.
#
# For example, with the values above, you'd print:
# I wanna be your endgame
# I wanna be your first string
# I wanna be your A-Team
# I wanna be your endgame, endgame
# I wanna be your endgame
# I wanna be your first string
# MAKE IT STOP
#
# That's 6 lines: the entire list once, then the first two lines
# again to reach 6. As before, print MAKE IT STOP when you're
# done.
#
# HINT: There are multiple ways to do this: some involve a small
# change to our earlier answer, others involve a more wholesale
# rewrite. If you're stuck on one, try to think of a totally
# different way!


# Add your code here! Using the initial inputs from above, this
# should print 7 lines: all 4 lines of the list, then the first
# two lines again, then MAKE IT STOP

counter = 0

while counter < lines_of_sanity:
    for item in lyrics:
        print(item)
        counter += 1
        if counter == lines_of_sanity:
            break

print("MAKE IT STOP")
