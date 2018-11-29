dosage = 100
time_since_last_dose = 7
is_nighttime = False
took_something_cross_reactive = False

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Let's try to use our mathematical operators and logical
# operators together.
#
# Imagine you've been battling a cold. You're deciding whether
# to take cough syrup or not, and if so, how much to take.
#
# time_since_last_dose represents the number of hours since
# you last took some cough syrup. For every hour it's been,
# you're allowed to have one dose.
#
# If it's nighttime (is_nighttime), then you may double
# your dose since you won't be taking any until morning.
#
# However, if you've taken something cross-reactive
# (took_something_cross_reactive), then you should not take
# any cough syrup.
#
# Write a program that will print how large a dose of cough
# syrup to take.
#
# HINT: Remember, if you try to multiply a number times a
# boolean, Python treats False as 0 and True as 1. There are
# other ways to do this, though.


# Add your code here!

if took_something_cross_reactive:
    suggested_dosage = 0
elif is_nighttime:
    suggested_dosage = time_since_last_dose * dosage * 2
else:
    suggested_dosage = time_since_last_dose * dosage

print(suggested_dosage)
