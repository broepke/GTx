# We've learned a lot in this chapter. Let's try to use a lot
# of it for one final exercise.
#
# Write a function called sort_artists. sort_artists will
# take as input a list of tuples. Each tuple will have two
# items: the first item will be a string holding an artist's
# name, and the second will be an integer representing their
# total album sales (in millions).
#
# Return a tuple of two lists. The first list in the
# resulting tuple should be all the artists sorted
# alphabetically. The second list should be all the revenues
# sorted in descending numerical order.
#
# For example:
# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#
# Notice that artists is a list of tuples (brackets first,
# then parentheses), but sort_artists outputs a tuple of
# lists (parentheses first, then brackets).


# Write your function here!
def sort_artists(a_list):

    result_tuple = ()
    artists_list = []
    revenue_list = []

    for i in a_list:
        artists_list.append(i[0])
        revenue_list.append(i[1])

    artists_list.sort()
    revenue_list.sort()
    revenue_list.reverse()

    result_tuple = (artists_list, revenue_list)

    return result_tuple

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# (['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))
