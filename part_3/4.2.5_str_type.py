# Write a function called 'string_type' which accepts one
# string argument and determines what type of string it is.
#
# - If the string is empty, return "empty".
# - If the string is a single character, return "character".
# - If the string represents a single word, return "word".
#   The string is a single word if it has no spaces.
# - If the string is a whole sentence, return "sentence".
#   The string is a sentence if it contains spaces, but
#   at most one period.
# - If the string is a paragraph, return "paragraph". The
#   string is a paragraph if it contains both spaces and
#   multiple periods (we won't worry about other
#   punctuation marks).
# - If the string is multiple paragraphs, return "page".
#   The string is a paragraph if it contains any newline
#   characters ("\n").
#
# Hint: think carefully about what order you should check
# these conditions in.
#
# Hint 2: remember, there exists a count() method that
# counts the number of times a string appears in another
# string. For example, "blah blah blah".count("blah")
# would return 3.


# Write your function here!
def string_type(a_string):
    if a_string.find("\n") > 0 and a_string.count(" ") > 0 and a_string.count(".") > 0:
        return "page"
    elif a_string.count(" ") > 0 and a_string.count(".") > 1:
        return "paragraph"
    elif a_string.count(" ") > 1:
        return "sentence"
    elif len(a_string) > 1 and a_string.count(" ") == 0:
        return "word"
    elif len(a_string) == 1:
        return "character"
    elif len(a_string) == 0:
        return "empty"
    else:
        return "dunno"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# empty
# character
# word
# sentence
# paragraph
# page
print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type(
    "There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type(
    "Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))
