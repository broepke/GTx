hot = True
cold = False
rainy = True
windy = False
snowy = False

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine you're writing a clothing-recommendation app that
# makes suggestions based on the weather. It has booleans
# representing five different kinds of weather: hot, cold,
# rainy, windy, snowy.
#
# The app recommends four kinds of clothing:
#
# - a jacket, if it's either cold or windy.
# - boots, if it's cold and snowy.
# - flip flops, if it's hot, unless it's rainy.
# - a t-shirt, if it's hot, unless it's rainy or windy.
#
# Write some code below that will print four lines, one for
# each of the four types of clothing. Under the original
# values for the variables above, the lines should look
# like this:
#
# Jacket: False
# Boots: False
# Flip-Flops: False
# T-shirt: False
#
# The values (True and False) will differ based on the
# values assigned to hot, cold, windy, snowy, and rainy
# at the start of the program.
#
# Hint: To print these lines, you'll need to add the
# result of the expression to a string of the clothing item.
# To do that, we'll need to convert the boolean from the
# expression into a string.


# Add your code here!
print("Jacket:", str(cold or windy))
print("Boots:", str(cold and snowy))
print("Flip-Flops:", str(hot and not rainy))
print("T-shirt:", str(hot and not (rainy or windy)))
