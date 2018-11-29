# In Chapter 3.4, we wrote a function called find_pressure
# that calculated pressure given number of moles,
# temperature, volume, and optionally, a value for R. If no
# value was given for R, we assumed its value should be
# 0.082057.
#
# However, as written, that function could crash: what about
# when the user enters a Volume of 0? That would cause a
# ZeroDivisonError! (In addition to breaking the laws of
# physics, but there's no Python error for that.)
#
# Revise that find_pressure function to catch that error. If
# that error occurs, return the string "Volume must be
# greater than 0." Otherwise, the function should work just
# as it did before.
#
# Feel free to copy your answer to that exercise and work
# from there. If you'd prefer to start from scratch, remember:
# you're creating a function called find_pressure that returns
# a value for pressure given variables n, T, V, and optionally
# R, according to this formula:
#
# Pressure = (nRT) / V
#
# You may not use a conditional. R should have a default value
# of 0.082057.


# Write your function here!


def find_pressure(moles, temp, volume, R=0.082057):
    try:
        return moles * R * temp / volume
    except ZeroDivisionError:
        return "Volume must be greater than 0."


# You may use these lines to test your function. With the
# values initially supplied here, your function should return
# "Volume must be greater than 0."
test_n = 10
test_T = 298
test_V = 0
test_R = 62.364  # Torr!
print(find_pressure(test_n, test_T, test_V, R=test_R))



