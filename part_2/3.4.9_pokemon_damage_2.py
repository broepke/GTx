# Recall Coding Problem 2.4.4. In that problem, you calculated
# the damage done by an attack based on several parameters.
#
# Convert your code from there into two functions, one called
# calculate_damage and one called calculate_modifier.
#
# Your function for calculate_damage must call calculate_modifier;
# it may not calculate the modifier separately. As such,
# calculate_damage should accept all ten parameters: STAB,
# Type, Critical, Other, Random, Level, Attack, Defense, and
# Base. You'll need to pass STAB, Type, Critical, Other, and
# Random to calculate_modifier.
#
# Make sure the parameters to each function follow the order
# shown above.
#
# As a reminder, damage is calculated using this formula:
# courses.edx.org/asset-v1:GTx+CS1301xII+1T2018+type@asset+block@DamageCalc.png
#
# Modifier is calculated using this formula:
# https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png


# Add your code here!


def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    Modifier = calculate_modifier(STAB, Type, Critical, Other, Random)

    dOne = (2 * Level + 10) / 250
    dTwo = Attack / Defense

    Damage = dOne * dTwo * Base + 2
    Damage = Damage * Modifier

    return Damage


def calculate_modifier(STAB, Type, Critical, Other, Random):
    Modifier = STAB * Type * Critical * Other * Random

    return Modifier


# Below are some lines of code that will test your function.
# You can change the value of the variable to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 16.0

STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))
