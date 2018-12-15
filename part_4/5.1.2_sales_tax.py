# In many areas, different goods are taxed at different rates.
# Areas may charge higher tax rates for items like alcohol,
# gasoline, and soda, and lower tax rates for items like
# grocery items, medicines, and clothes.
#
# Write a class called PurchasedGood. The constructor for
# PurchasedGood should have one positional parameter called
# price, which is the price of the good as a float. It should
# then have two keyword parameters in this order:
# - category, which is the category the good falls into.
#   category should have a default value of "General".
# - tax, which is the sales tax rate. tax should have a
#   default value of 0.07.
#
# These three values should be stored in attributes called
# 'price', 'category', and 'tax'.
#
# Then, add a method called calculate_total. calculate_total
# should calculate the price plus the price times the tax
# rate, then round the result to 2 decimal places and return
# the result. Remember, you can round to two decimal places
# using round(total, 2).


# Add your class here!
class PurchasedGood:
    def __init__(self, price, category="General", tax=0.07):
        self.price = price
        self.category = category
        self.tax = tax

    def calculate_total(self):
        return round(self.price * (1 + self.tax),2)

# Below are some lines of code that will test your object.
# You can change these lines to test your code in different
# ways.
#
# If your code works correctly, this will originally run
# error-free and print ignoring rounding errors):
# 5.0
# General
# 0.07
# 5.35
# 5.0
# Grocery
# 0.03
# 5.15
good_1 = PurchasedGood(5.00)
print(good_1.price)
print(good_1.category)
print(good_1.tax)
print(good_1.calculate_total())

good_2 = PurchasedGood(5.00, category="Grocery", tax=0.03)
print(good_2.price)
print(good_2.category)
print(good_2.tax)
print(good_2.calculate_total())
