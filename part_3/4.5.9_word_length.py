# Recall last exercise that you wrote a function, word_lengths,
# which took in a string and returned a dictionary where each
# word of the string was mapped to an integer value of how
# long it was.
#
# This time, write a new function called length_words so that
# the returned dictionary maps an integer, the length of a
# word, to a list of words from the sentence with that length.
# If a word occurs more than once, add it more than once. The
# words in the list should appear in the same order in which
# they appeared in the sentence.
#
# For example:
#
#  length_words("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
# As before, you should remove any punctuation and make the
# string lowercase.
#
# Hint: To create a new list as the value for a dictionary key,
# use empty brackets: lengths[wordLength] = []. Then, you would
# be able to call lengths[wordLength].append(word). Note that
# if you try to append to the list before creating it for that
# key, you'll receive a KeyError.


# Write your function here!
def length_words(a_string):
    a_string = a_string.replace(".", "")
    a_string = a_string.replace("!", "")
    a_string = a_string.replace("'", "")
    a_string = a_string.replace(",", "")
    a_string = a_string.replace("?", "")
    a_string = a_string.lower()

    string_list = a_string.split()
    string_dict = {}

    for word in string_list:
        try:
            if string_dict[len(word)]:
                string_dict[len(word)].append(word)

        except:
            string_dict[len(word)] = []
            string_dict[len(word)].append(word)

    return string_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# {1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
# The keys may appear in a different order, but within each
# list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))
