# In the Pokemon video game series, every Pokemon has six
# stats: HP, Attack, Defense, Special Attack, Special Defense,
# and Speed.
#
# Write a function called total_stats that will take as input
# a list of dictionaries. Each dictionary will have seven
# key-value pairs:
#
# - name: a Pokemon's name
# - hp, attack, defense, special attack, special defense,
#   and speed: an integer representing that Pokemon's stat
#   in that category
#
# Your function should return a single dictionary. The keys
# of the dictionary should be the Pokemon names from the
# original list, and the values should be the _total_ stats
# for each Pokemon (add HP, Attack, Defense, Special Attack,
# Special Defense, and Speed).
#
# For example, if this was one of the dictionaries in the
# original list:
#
# {"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49,
# "special attack": 65, "special defense": 65, "speed": 45}
#
# Then one of the key-value pairs in the dictionary you
# return would be: "Bulbasaur": 318 (45 + 49 + 49 + 65 + 65 +
# 45 = 318).


# Add your function here!
def total_stats(starters):
    new_dict = {}

    for dudes in starters:
        total = 0
        for keys in dudes.keys():
            if not keys == "name":
                total += dudes[keys]
        new_dict[dudes["name"]] = total

    return new_dict


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'Bulbasaur': 318, 'Charmander': 309, 'Squirtle': 314}
starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65,
             "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50,
             "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64,
             "speed": 43}]
print(total_stats(starters))
