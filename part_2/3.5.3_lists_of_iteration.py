given_items = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

# Write a program that iterates through the items in the
# given list. For each item, you should attempt to iterate
# through the item and print each character seperately.
#
# If this second part fails, print "Not iterable" -- but
# even if the second part fails, you should still go on
# to the next item in the list.
#
# Hint: Although we'll cover lists more in Unit 4, all
# you need to know right now is that this syntax will run
# a loop over a list, a string, or any other iterable
# type of information:
#
#  for item in given_items:
#
# To iterate over the items in 'item', you can do the
# same thing: for subitem in item:
#
# Start out by building the nested for-each loops that
# you'll need. Then, identify where the error is
# occurring to figure out where to put the try-except
# structure.
#
# This one's tricky, but you can do it!


# Add your code here!


for item in given_items:
    try:
        for char in item:
            print(char)
    except:
        print("Not iterable")
