meal_cost = 10.00
tax_rate = 0.08
tip_rate = 0.20

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# When eating at a restaurant in the United States, it's
# customary to have two percentage-based surcharges added on
# top of your bill: sales tax and tip. These percentages are
# both applies to the original cost of the meal. For example,
# a 10.00 meal with 8% sales tax and 20% tip would add 0.80
# for tax (0.08 * 10.00) and 2.00 for tip (0.20 * 10.00).
#
# The variables above create the cost of a meal and identify
# what percentage should be charged for tax and tip.
#
# Add some code below that will print the "receipt" for a
# meal purchase. The receipt should look like this:
#
# Subtotal: 10.00
# Tax: 0.8
# Tip: 2.0
# Total: 12.8
#
# Subtotal is the original value of meal_cost, tax is the
# tax rate times the meal cost, tip is the tip rate times
# the meal cost, and total is the sum of all three numbers.
# Don't worry about the number of decimal places; it's fine
# if your code leaves off some numbers (like 0.8 for tax) or
# includes too many decimal places (like 2.121212121 for tip).


# Add your code here!
print("Subtotal:", meal_cost)
print("Tax:", meal_cost * tax_rate)
print("Tip:", meal_cost * tip_rate)
print("Total:", (meal_cost + (meal_cost * tax_rate)) + (meal_cost * tip_rate))
