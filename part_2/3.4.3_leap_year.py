# A year is considered a leap year if it abides by the
# following rules:
#
#  - Every 4th year IS a leap year, EXCEPT...
#  - Every 100th year is NOT a leap year, EXCEPT...
#  - Every 400th year IS a leap year.
#
# This starts at year 0. For example:
#
#  - 1993 is not a leap year because it is not a multiple of 4.
#  - 1996 is a leap year because it is a multiple of 4.
#  - 1900 is not a leap year because it is a multiple of 100,
#    even though it is a multiple of 4.
#  - 2000 is a leap year because it is a multiple of 400,
#    even though it is a multiple of 100.
#
# Write a function called is_leap_year. is_leap_year should
# take one parameter: year, an integer. It should return the
# boolean True if that year is a leap year, the boolean False
# if it is not.


# Write your function here!
def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print False, True, False, and True, each preceded by the
# label "[year] is a leap year:".
print("1993 is a leap year:", is_leap_year(1993))
print("1996 is a leap year:", is_leap_year(1996))
print("1900 is a leap year:", is_leap_year(1900))
print("2000 is a leap year:", is_leap_year(2000))
