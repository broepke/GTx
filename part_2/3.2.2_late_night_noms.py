hour = 3
minute = 45

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Around Georgia Tech, there are plenty of places to get a
# late night bite to eat. However, they have different hours,
# so when choosing where to go, you have to think about who's
# still open!
#
# Imagine you're choosing between the following restaurants:
#
# - Barrelhouse: Closes at 11:00PM
# - Taco Bell: Closes at 2:00AM
# - Cookout: Closes at 3:00AM
# - Waffle House: Never closes. Ever.
#
# Assume that this list is also a priority list: if Barrelhouse
# is open, you choose Barrelhouse. If not, you choose Taco Bell
# if it's open. If not, you choose Cookout if it's open. If
# not, you choose Waffle House.
#
# However, there are two wrinkles:
#
# - We're using 12-hour time.
# - hour will always represent a time from 10PM to 5AM.
#
# That means that if hour is 10 or 11, it's PM; if hour is
# 12, 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
# a little more complex. You may assume that all four
# restaurants open later than 6AM, though, so you don't have
# to worry about opening time, just closing time.
#
# Add some code below that will print what restaurant you'll
# go to based on the current values of hour and minute.


# Add your code here!
if hour >= 6 and hour < 11:
    print("Barrelhouse")
elif hour >= 11 or (hour >= 1 and hour < 2):
    print("Taco Bell")
elif hour >= 2 and hour < 3:
    print("Cookout")
else:
    print("Waffle House")
