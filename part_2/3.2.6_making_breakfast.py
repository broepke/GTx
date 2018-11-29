egg = True
milk = True
butter = True
flour = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine you're deciding what you want to cook. The boolean
# variables above state whether or not you have each of those
# four ingredients.
#
# Here are the dishes you know how to cook and their
# ingredients:
#
# 1. pancakes: egg, milk, butter, flour
# 2. omelette: egg, milk, butter
# 3. custard: egg, milk
# 4. poached eggs: egg
#
# The list above is also a priority list. If you have the
# ingredients for pancakes, you'll make pancakes instead of
# any of the other dishes. If you're missing flour but have
# the other ingredients, you'll make an omlette. You'll only
# make poached eggs if the only ingredient you have is eggs.
#
# Complete the program below such that it prints which dish
# you'll make based on the ingredients you have handy. All
# the dishes should appear exactly as shown above: all lower
# case, spelled the same way. If you do not have the
# ingredients to make any of these dishes, then print the
# text "Go to the store!"


# Add your code here!
if egg and milk and butter and flour:
    print("pancakes")
elif egg and milk and butter:
    print("omelette")
elif egg and milk:
    print("custard")
elif egg:
    print("poached eggs")
else:
    print("Go to the store!")
