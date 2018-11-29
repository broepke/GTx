words = ["dog", "sparrow", "cat", "frog"]

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# This program is supposed to print the location of the 'o'
# in each word in the list. However, line 18 causes an
# error if 'o' is not in the word. Add try/except blocks
# to print "Not found" when the word does not have an 'o'.
# However, when the current word does not have an 'o', the
# program should continue to behave as it does now.
#
# Hint: don't worry that you don't know how line 18 works.
# All you need to know is that it may cause an error.
#
# You may not use any conditionals.


# Fix this code!

for word in words:
    try:
        print(word.index("o"))
    except:
        print("Not found")
