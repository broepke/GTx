# Write a function called average_word_length that takes as
# input a string called my_string, and returns as output the
# average length of the words in the string.
#
# In writing this function, note the following:
#
# - You should account for consecutive spaces. A string like
#   "Hi   Lucy" is two words with an average length of 3.0
#   characters.
# - You should not assume the string starts with a letter.
#   A string like "  David" has one word with an average
#   length of 5.0 characters.
# - You should not count punctuation marks toward the
#   length of a word. A string like "Hi, Lucy" has two
#   words with an average length of 3.0 characters: the ,
#   after "Hi" does not count as a character in the word.
#   The only punctuation marks you need to handle are
#   these: . , ! ?
# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If my_string is not a string, you should instead return
#   the string, "Not a string".
# - If there are no words in my_string, you should instead
#   return the string, "No words". This could happen for
#   strings like "" (an empty string) and ".,!?" (a string
#   of only punctuation marks). You may assume that any
#   of these punctuation marks will always be followed by
#   at least one space.
#
# Here are a few hints that might help you:
#
# - You can peak at the first character in my_string with
#   my_string[0]. If my_string is "Hi, Lucy", then the value
#   of my_string[0] is "H". You don't have to do this, but
#   you can if you want.
# - There are lots of ways you can do this. If you're
#   stuck, try taking a step back and thinking about the
#   problem from a fresh perspective.
# - If you're still stuck, try counting words and letters
#   separately, and worrying about average length only
#   after both have been counted.
# - The word count should equal the number of letters that
#   come immediately after a space or the start of the
#   string. The character count should simply equal the
#   number of characters besides spaces and punctuation
#   marks. The average word length should be character
#   count divided by word count.


# Write your function here!
def average_word_length(my_string):

    my_average = 0
    my_word_count = 0
    my_char_count = 0

    #test to see if it's a string
    try:
        # find how many total valid letters
        my_char_count = count_alpha_chars(my_string)
    except TypeError:
        return "Not a string"

    #find how many words
    my_word_count = word_count(my_string)

    return my_char_count / my_word_count

#get the total number of words
def word_count(my_string):

    counter = 0
    last_char = ""
    first_char_space = False

    if my_string[0] == " ":
        first_char_space = True

    try:
        for i in my_string:
            if i == " ":
                if last_char != i:
                    counter += 1
            last_char = i
        if first_char_space:
            return counter
        else:
            return counter + 1
    except:
        return "Not a string"

def count_alpha_chars(my_string):

    char_count = 0

    for i in my_string:
        if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            char_count += 1

    return char_count


# When your function works, the following code should
# output:
# 2.0
# 3.0
# 4.0
# Not a string
# No words

print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))

