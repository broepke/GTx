# -----------------------------------------------------------
# The United States Social Security Administration publishes
# a list of all documented baby names each year, along with
# how often each name was used for boys and for girls. The
# list is used to see what names are most common in a given
# year.
#
# We've grabbed that data for any name used more than 25
# times, and provided it to you in a file called
# babynames.csv. The line below will open the file:

# names_file = open('../resource/lib/public/babynames.csv', 'r')

names_file = open("baby_names.csv", "r")

names = {}
largest = 0
largest_name = ""

for lines in names_file:
    lines = lines.rstrip("\n")
    line_list = lines.split(",")
    try:
        names[line_list[0]] += int(line_list[1])
    except:
        names[line_list[0]] = int(line_list[1])

for (keys, values) in names.items():
    if values > largest:
        largest = values
        largest_name = keys

print(largest_name, largest) #Isabella 42623

names_file.close()

# We've also provided a sample subset of the data in
# sample.csv.
#
# Each line of the file has three values, separated by
# commas. The first value is the name; the second value is
# the number of times the name was given in the 2010s (so
# far); and the third value is whether that count
# corresponds to girls or boys. Note that if a name is
# given to both girls and boys, it is listed twice: for
# example, so far in the 2010s, the name Jamie has been
# given to 611 boys and 1545 girls.
#
# Use this dataset to answer the questions below.


# Here, add any code you want to allow you to answer the
# questions asked below over on edX. This is just a sandbox
# for you to explore the dataset: nothing is required for
# submission here.

# How many total names are listed in the database?
# counter = 0
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     counter += 1
#
# print(counter) #15790

# How many total births are covered by the names in the database?
# total_births = 0
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     total_births += int(line_list[1])
#
# print(total_births) # 7030332

# How many different boys' names are there that begin with the letter Z? (Count the names, not the people.)
# total_z_boys = 0
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if line_list[0][:1] == "Z" and line_list[2] == "Boy":
#         total_z_boys += 1
#
# print(total_z_boys) #159

# What is the most common girl's name that begins with the letter Q?
# q_names = {}
# largest = 0
# largest_name = ""
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if line_list[0][:1] == "Q" and line_list[2] == "Girl":
#         try:
#             q_names[line_list[0]] += int(line_list[1])
#         except:
#             q_names[line_list[0]] = int(line_list[1])
#
#
# for (keys, values) in q_names.items():
#     if values > largest:
#         largest = values
#         largest_name = keys
#
#
# print(largest_name, largest) # Quinn 2954


# How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?
# first_letter = ""
# last_letter = ""
# vowels = ["a", "e", "i", "o", "u"]
# total = 0
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     first_letter = line_list[0][:1]
#     last_letter = line_list[0][-1:]
#     first_letter = first_letter.lower()
#     last_letter = last_letter.lower()
#     if first_letter in vowels and last_letter in vowels:
#         total += int(line_list[1])
#
# print(total) # 672960

# What letter is the least common first letter of a baby's name (in terms of
# number of babies with names starting with that letter, not number of names)?
# How many babies were born with names starting with that least-common letter?
#
# names = {}
# smallest = 100000000000000000
# smallest_name = ""
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     try:
#         names[line_list[0][:1]] += int(line_list[1])
#     except:
#         names[line_list[0][:1]] = int(line_list[1])
#
# for (keys, values) in names.items():
#     if values < smallest:
#         smallest = values
#         smallest_name = keys
#
# print(smallest_name, smallest) # U 6283


# What letter is the most common first letter of a baby's name
# (in terms of number of babies with names starting with that letter, not number of names)?
#
# names = {}
# largest = 0
# largest_name = ""
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     try:
#         names[line_list[0][:1]] += int(line_list[1])
#     except:
#         names[line_list[0][:1]] = int(line_list[1])
#
# for (keys, values) in names.items():
#     if values > largest:
#         largest = values
#         largest_name = keys
#
# print(largest_name, largest) # A 983627


# By default, the Social Security Administration's data separates out names by gender.
# For example, Jamie is listed separately for girls and for boys. If you were to remove this separation,
# what would be the most common name in the 2010s regardless of gender?

# names = {}
# largest = 0
# largest_name = ""
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     try:
#         names[line_list[0]] += int(line_list[1])
#     except:
#         names[line_list[0]] = int(line_list[1])
#
# for (keys, values) in names.items():
#     if values > largest:
#         largest = values
#         largest_name = keys
#
# print(largest_name, largest) #Isabella 42623

# What name that is used for both genders has the smallest difference in
# which gender holds the name most frequently? In case of a tie, enter any one of the correct answers.
#
# names = {}
# smallest_delta = 100000000000
# smallest_name = ""
#
# for lines in names_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     try:
#         names[line_list[0]][line_list[2]] = int(line_list[1])
#     except:
#         names[line_list[0]] = {line_list[2]: int(line_list[1])}
#
# for (keys, values) in names.items():
#     try:
#         if abs(values["Girl"] - values["Boy"]) < smallest_delta:
#             smallest_delta = abs(values["Girl"] - values["Boy"])
#             smallest_name = keys
#     except:
#         pass
#
# print(smallest_delta, smallest_name)  #Tatem