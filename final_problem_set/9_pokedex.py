pokedex = open("pokedex.csv", "r")

types = {}
highest_average = 0
highest_average_type = ""
sum = 0
ave = 0

for lines in pokedex:
    lines = lines.rstrip("\n")
    line_list = lines.split(",")
    if not line_list[0] == "Number":
        try:
            types[line_list[2]].append(line_list[9])
        except:
            types[line_list[2]] = [line_list[9]]

for (key, value) in types.items():
    sum = 0
    ave = 0
    for i in range(len(value)):
        sum += int(value[i])
    ave = sum / len(value)
    if ave > highest_average:
        highest_average = ave
        highest_average_type = key

print(highest_average_type, round(highest_average))  # Flying 102

pokedex.close()

# We've also provided a sample subset of the data in
# sample.csv.
#
# Each line of the file has 13 values, separated by commas.
# They are:
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
# Use this dataset to answer the questions below.


# Here, add any code you want to allow you to answer the
# questions asked below over on edX. This is just a sandbox
# for you to explore the dataset: nothing is required for
# submission here.


# How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
#
# blanks = 0
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         if line_list[3] == "":
#             blanks += 1
#
# print(blanks) #420

# What is the most common type? Include both Type1 and Type2 in your count.
#
# types = {}
# most_common_type = 0
# most_common = ""
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         try:
#             types[line_list[2]] += 1
#         except:
#             types[line_list[2]] = 1
#         if not line_list[3] == "":
#             try:
#                 types[line_list[3]] += 1
#             except:
#                 types[line_list[3]] = 1
#
# for key, value in types.items():
#     if value > most_common_type:
#         most_common_type = value
#         most_common = key
#
# print(most_common, most_common_type) # Water 140

# What Pokemon has the highest HP statistic?
# high_hp = 0
# high_hp_card = ""
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         if int(line_list[4]) > high_hp:
#             high_hp = int(line_list[4])
#             high_hp_card = line_list[1]
#
#
# print(high_hp, high_hp_card) # 255 Blissey

# Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?

# high_hp = 0
# high_hp_card = ""
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         if line_list[11] == "FALSE" and line_list[12] == "FALSE":
#             if int(line_list[6]) > high_hp:
#                 high_hp = int(line_list[6])
#                 high_hp_card = line_list[1]
#
#
# print(high_hp, high_hp_card) # 230 Shuckle

# Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.

# types = {}
# most_common_type = 0
# most_common = ""
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         if line_list[11] == "TRUE":
#             try:
#                 types[line_list[2]] += 1
#             except:
#                 types[line_list[2]] = 1
#             if not line_list[3] == "":
#                 try:
#                     types[line_list[3]] += 1
#                 except:
#                     types[line_list[3]] = 1
#
# for key, value in types.items():
#     if value > most_common_type:
#         most_common_type = value
#         most_common = key
#
# print(most_common, most_common_type) # Psychic 32

# In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed),
# what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.
#
# total_stats = 0
# weakest = 9999999
# weakest_card = ""
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         if line_list[11] == "TRUE":
#             total_stats = int(line_list[4]) + int(line_list[5]) + int(line_list[6]) + int(line_list[7]) + int(line_list[8]) + int(line_list[9])
#             if total_stats < weakest:
#                 weakest = total_stats
#                 weakest_card = line_list[1]
#
#
#
# print(weakest_card, weakest) #Cosmog 200

# In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed),
# what is the strongest non-Legendary, non-Mega Pokemon? If there is a tie, list any of the tying Pokemon.

# total_stats = 0
# strongest = 0
# strongest_card = ""
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         if line_list[11] == "FALSE" and line_list[12] == "FALSE":
#             total_stats = int(line_list[4]) + int(line_list[5]) + int(line_list[6]) + int(line_list[7]) + int(
#                 line_list[8]) + int(line_list[9])
#             if total_stats > strongest:
#                 strongest = total_stats
#                 strongest_card = line_list[1]
#
# print(strongest_card, strongest)  # Slaking 670


# What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.
#
# types = {}
# highest_average = 0
# highest_average_type = ""
# sum = 0
# ave = 0
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         try:
#             types[line_list[2]].append(line_list[9])
#         except:
#             types[line_list[2]] = [line_list[9]]
#
# for (key, value) in types.items():
#     for i in range(len(value)):
#         sum += int(value[i])
#     ave = sum / len(value)
#     if ave > highest_average:
#         highest_average = ave
#         highest_average_type = key
#
# print(highest_average_type, highest_average)  #Flying


# # Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation.
#
# types = {}
# highest_average = 0
# highest_average_type = ""
# sum = 0
# ave = 0
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         try:
#             types[line_list[2]].append(line_list[9])
#         except:
#             types[line_list[2]] = [line_list[9]]
#
# for (key, value) in types.items():
#     sum = 0
#     ave = 0
#     for i in range(len(value)):
#         sum += int(value[i])
#     ave = sum / len(value)
#     if ave > highest_average:
#         highest_average = ave
#         highest_average_type = key
#
# print(highest_average_type, round(highest_average))  # Flying 102

# Among all 7 Pokemon generations, which generation had the highest average sum of all six stats
# (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

# Rounded to the nearest integer, how much higher was that statistic than the next-closest generation's
# average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

# types = {}
# total_stats = 0
# avg = 0
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         total_stats = int(line_list[4]) + int(line_list[5]) + int(line_list[6]) + int(line_list[7]) + int(
#             line_list[8]) + int(line_list[9])
#         try:
#             types[line_list[10]].append(total_stats)
#         except:
#             types[line_list[10]] = [total_stats]
#
# for (key, value) in types.items():
#     total = 0
#     for i in value:
#         total += i
#     avg = total / len(value)
#     print(key, round(avg))

# 5 435
# 1 427
# 4 459 <
# 3 436
# 6 438
# 7 461 <<
# 2 418


# Rounded to the nearest integer, how much higher is the average sum of all six stats
# among Mega Pokemon than their non-Mega versions? Note that Mega Pokemon share the
# same Number (the first column) as their non-Mega versions, which will allow you to
# find all Pokemon that have a Mega version.
#
# types = {}
# total_stats = 0
# avg = 0
# delta = 0
#
# for lines in pokedex:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Number":
#         total_stats = int(line_list[4]) + int(line_list[5]) + int(line_list[6]) + int(line_list[7]) + int(
#             line_list[8]) + int(line_list[9])
#         try:
#             types[line_list[0]].append(total_stats)
#         except:
#             types[line_list[0]] = [total_stats]
#
# for (key, value) in types.items():
#     total = 0
#     if len(value) == 2:
#         delta = value[1] - value[0]
#         delta = abs(delta)
#         print(key, round(delta))
