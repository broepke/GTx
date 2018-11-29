start_character = "A"
end_character = "Z"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Print all the letters from start_character to end_character,
# each on their own line. Include start_character and
# end_character themselves.
#
# Remember, you can convert a letter to its underlying ASCII
# number using the ord() function. ord("A") would give 65.
# ord("Z") would give 90. You can use these values to write
# your loop.
#
# You can also convert an integer into its corresponding ASCII
# character using the chr() function. chr(65) would give "A".
# chr(90) would give "Z". So, for this problem, you'll need
# to convert back and forth between ordinal values and
# characters based on whether you're trying to loop over
# numbers or print letters.
#
# You may assume that both start_character and end_character
# are uppercase letters (although you might find it fun to
# play around and see what happens if you put other characters
# in instead!).


# Add your code here! With the original values for
# start_character and end_character, this will print the
# letters from A to Z, each on their own line.

counter = ord(start_character)

for i in range(ord(start_character), ord(end_character) + 1):
    print(chr(i))
