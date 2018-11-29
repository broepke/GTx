# In chemistry, the ideal gas law states:
#
# pressure * volume = # of moles * gas constant * temperature
#
# This is usually abbreviated to:
#
# PV = nRT
#
# We can solve this for any of these five variables, but let's
# solve it for Pressure. In terms of Pressure, the ideal gas
# law states:
#
# P = (nRT) / V
#
# Write a function called find_pressure that takes as input
# three variables: number of moles, temperature, and volume.
# You can call these variables in the function whatever you
# want, but they must be specified in that order: moles, then
# temperature, then volume. You should assume all three are
# floats. Then, return as output your calculation for
# pressure. For the gas constant, you should use the value
# 0.082057.
#
# Hint: Python's rounding errors can change based on the
# order of the multipliers. If you're having difficulty with
# your answer being off by tiny fractions, change the order
# of the numbers to match the order in the formula above.


# Write your function here!
def find_pressure(moles, temp, volume):
    return moles * 0.082057 * temp / volume


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "Result: 48.905972000000006". The extra zeroes and
# the 6 are rounding errors by Python.
test_n = 10
test_T = 298
test_V = 5
print("Result:", find_pressure(test_n, test_T, test_V))
