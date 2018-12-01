# Write a function called string_finder. string_finder should
# take two parameters: a target string and a search string.
# The function will look for the search string within the
# target string.
#
# The function should return a string representing where in
# the target string the search string was found:
#
# - If search string is at the very beginning of target
#   string, then return "Beginning". For example:
#   string_finder("Georgia Tech", "Georgia") -> "Beginning"
#
# - If search string is at the very end of target string,
#   then return "End". For example:
#   string_finder("Georgia Tech", "Tech") -> "End"
#
# - If search string is in target string but not at the
#   very beginning or very end, then return "Middle. For
#   example:
#   string_finder("Georgia Tech", "gia") -> "Middle"
#
# - If search string is not in target string at all, then
#   return "Not found". For example:
#   string_finder("Georgia Tech", "Idaho") -> "Not found"
#
# Assume that we're only interested in the first instance
# of the search string if it appears multiple times in the
# target string, and that search string is definitely
# shorter than target string.
#
# Hint: Don't be surprised if you find that the "End" case
# is the toughest! You'll need to look at the lengths of
# both the target string and the search string.


# Write your function here!
def string_finder(target_str, search_str):
    if target_str.find(search_str) >= 0:
        location = target_str.find(search_str)
    else:
        return "Not found"

    if location == 0:
        return "Beginning"

    elif location == len(target_str) - len(search_str):
        return "End"

    else:
        return "Middle"





# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Start, Middle, End, Not found, each on their own
# line.
print(string_finder("Georgia Tech", "Georgia"))
print(string_finder("Georgia Tech", "gia"))
print(string_finder("Georgia Tech", "Tech"))
print(string_finder("Georgia Tech", "Idaho"))
