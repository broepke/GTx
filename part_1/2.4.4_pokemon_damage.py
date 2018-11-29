STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60


# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# In the Pokemon game franchise, damage is calculated using this formula:
# https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@DamageCalc.png
#
# In that formula, the variable Modifier is calculated using this formula:
# https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png
#
# Add code below such that the program prints the total damage
# caused based on the STAB, Type, Critical, Other, Random,
# Level, Attack, Defense, and Base given above.
#
# Hint: Don't try to do all these calculations at once! Break
# the complicated formula down into bite-sized little chunks.


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


# Add your code here!
dOne = (2 * Level + 10) / 250
dTwo = Attack / Defense

Modifier = STAB * Type * Critical * Other * Random

Damage = dOne * dTwo * Base + 2
Damage = Damage * Modifier

print(Damage)
