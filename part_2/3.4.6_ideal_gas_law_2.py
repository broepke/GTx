# Last problem, we wrote a function that calculated pressure
# given number of moles, temperature, and volume. We told you
# to assume a value of 0.082057 for R. This value means that
# pressure must be given in atm, or atmospheres, one of the
# common units of measurement for pressure.
#
# atm is the most common unit for pressure, but there are
# others: mmHg, Torr, Pa, kPa, bar, and mb, for example. what
# if pressure was sent in using one of these units? Our
# calculation would be wrong!
#
# So, we want to *assume* that pressure is in atm (and thus,
# that R should be 0.082057), but we want to let the person
# calling our function change that if need be. So, revise
# your find_pressure function so that R is a keyword parameter.
# Its default value should be 0.082057, but the person calling
# the function can override that. The name of the parameter for
# the gas constant must be R for this to work.
#
# As a reminder, you're writing a function that calculates:
#
# P = (nRT) / V
#


# Write your function here! You may copy your work from 3.4.5
# if you'd like.
def find_pressure(moles, temp, volume, R=0.082057):
    return moles * R * temp / volume


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "Result: 37168.944".
test_n = 10
test_T = 298
test_V = 5
test_R = 62.364  # Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R=test_R))
