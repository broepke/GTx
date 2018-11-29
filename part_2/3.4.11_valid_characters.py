# There are a lot of use cases where we want to check to see
# if a string has any invalid characters in it. For example,
# when asking for a credit card number, we want to make sure
# there are no non-numerals (although we might accept dashes
# or spaces). When asking for a name, we want to make sure
# all the characters are letters, spaces, or the occasional
# punctuation mark.
#
# Write a function called is_valid. is_valid should take two
# parameters: a string to check, and a string of all valid
# characters.
#
# is_valid should return the boolean True if all the
# characters in the string to check are present in the string
# of valid characters. It should return False if any character
# in the checked string does not appear.


# Add your code here!

def is_valid(chk_string, valid_chars):
    for i in chk_string:
        if valid_chars.find(i) < 0:
            return False

    return True


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print True, then False
sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))
