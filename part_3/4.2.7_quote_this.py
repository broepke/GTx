# Write a function called "quote_this" that accepts two
# strings as arguments: a string representing a quote and
# a string of a name. The function should return a new
# string with the quote surrounded by quotation marks (")
# followed by a dash and the given name. For example:
#
# a = quote_this("Try and fail, but never fail to try.",
# "Jared Leto")
# print(a)
#
# Will print:
# "Try and fail, but never fail to try." -Jared Leto
#
# If the code were to continue, this:
#
# b = quote_this(a, "Michael Scott")
# print(b)
#
# Would print:
# ""Try and fail, but never fail to try." -Jared Leto"
# - Michael Scott


# Write your function here!
def quote_this(quote, name):
    quote = "\"" + quote + "\""

    return quote + " -" + name


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print the same output as the examples above.
a = quote_this("Try and fail, but never fail to try.", "Jared Leto")
print(a)
b = quote_this(a, "Michael Scott")
print(b)
