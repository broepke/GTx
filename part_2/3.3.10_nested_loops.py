mystery_int = 5

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# This is a tough one! Stick with it, you can do it!
#
# Write a program that will print the times table for the
# value given by mystery_int. The times table should print a
# two-column table of the products of every combination of
# two numbers from 1 through mystery_int. Separate consecutive
# numbers with either spaces or tabs, whichever you prefer.
#
# For example, if mystery_int is 5, this could print:
#
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20
# 5	10	15	20	25
#
# To do this, you'll want to use two nested for loops; the
# first one will print rows, and the second will print columns
# within each row.
#
# Hint: How can you print the numbers across the row without
# starting a new line each time? With what you know now, you
# could build the string for the row, but only print it once
# you've finished the row. There are other ways, but that's
# how to do it using only what we've covered so far.
#
# Hint 2: To insert a tab into a string, use the character
# sequence "\t". For example, "1\t2" will print as "1	2".
#
# Hint 3: Need to just start a new line without printing
# anything else? Just call print() with no arguments in the
# parentheses.
#
# Hint 4: If you're stuck, try first just printing out all
# the products in one flat list, each on its own line. Once
# that's working, then worry about how to organize it into
# a table.


# Add your code here!

row_string = ""

# loop for each row
for col in range(1, mystery_int + 1):
    # print the row / columns
    for row in range(1, mystery_int + 1):
        row_string = row_string + str(col * row) + "\t"
    print(row_string)
    row_string = ""
