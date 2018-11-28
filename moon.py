phase = "Full"
distance = 243000
date = 26
eclipse = False

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# There are (at least) three special types of full moons:
#
# - Super Moon: the full moon occurs when the moon is at its
#   closest approach to earth (less than 230,000km away).
# - Blue Moon: the second full moon in a calendar month. In
#   other words, any full moon on the 29th, 30th, or 31st of
#   a month.
# - Blood Moon: a lunar eclipse during a full moon.
#
# Write a program that will print out the type of moon --
# "Full Moon", "Super Moon", "Blue Moon", "Blood Moon", based
# on the values of the variables above. Note that for the moon
# to be any of these special kinds of moons, it must also be
# full.
#
# Note, though, that multiple modifiers can be true at the same
# time. We could have a Super Blue Moon, a Blue Blood Moon, or
# even a Super Blue Blood Moon.
#
# Always print those modifiers in that order. If any of these
# special modifiers is present, do not include the word "Full".
# If none of them are present, but the moon is Full, then print
# "Full Moon". If none of them are present at all, print "Moon".


# Add your code here!
moon_type = "Moon"
other_than_full = False

if phase == "Full":
    if eclipse:
        moon_type = "Blood " + moon_type
        other_than_full = True

    if date == 29 or date == 30 or date == 31:
        moon_type = "Blue " + moon_type
        other_than_full = True

    if distance < 230000:
        moon_type = "Super " + moon_type
        other_than_full = True

    if not other_than_full:
        moon_type = "Full " + moon_type

print(moon_type)
