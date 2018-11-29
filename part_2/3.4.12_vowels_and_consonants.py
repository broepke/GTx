# In this problem, your goal is to write a function that can
# either count all the vowels in a string or all the consonants
# in a string.
#
# Call this function count_letters. It should have two
# parameters: the string in which to search, and a boolean
# called find_consonants. If find_consonants is True, then the
# function should count consonants. If it's False, then it
# should instead count vowels.
#
# Return the number of vowels or consonants in the string
# depending on the value of find_consonants. Do not count
# any characters that are neither vowels nor consonants (e.g.
# punctuation, spaces, numbers).
#
# You may assume the string will be all lower-case letters
# (no capital letters).


# Add your code here!

def count_letters(a_string, find_consonants):
    str_len = len(a_string)
    num_vowels = 0
    are_vowels = ["a", "e", "i", "o", "u"]
    num_spaces = 0
    total = 0

    # count the vowels
    for i in a_string:
        if i in are_vowels:
            num_vowels += 1

    # get the number of spaces
    for i in a_string:
        if i == " ":
            num_spaces += 1

    # generate the total
    if find_consonants:
        total = str_len - num_vowels - num_spaces
    else:
        total = num_vowels

    return total


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print 14, then 7.

a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))
