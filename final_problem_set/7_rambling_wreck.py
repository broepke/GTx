# Last problem, you wrote a function that generated the all-
# time win-loss-tie record for Georgia Tech against any other
# team.
#
# That dataset had a lot of other information in it. Let's
# use it to answer some more questions. As a reminder, the
# data will be a CSV file, meaning that each line will be a
# comma-separated list of values. Each line will describe one
# game.
#
# The columns, from left-to-right, are:
#
# - 0 Date: the date of the game, in Year-Month-Day format.
# - 1 Opponent: the name of the opposing team
# - 2 Location: Home, Away, or Neutral
# - 3 Points For: Points scored by Georgia Tech
# - 4 Points Against: Points scored by the opponent

# This line will open the file:
# record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')

record_file = open("spring2016.csv", 'r')
# 1 = Opponent, 3 = Points for, 4 = Against

points = {}
highest = 0
highest_team = ""
average_diff = 0

for lines in record_file:
    lines = lines.rstrip("\n")
    line_list = lines.split(",")
    if not line_list[0] == "Date":
        try:
            points[line_list[1]]["diff"] += abs(int(line_list[3]) - int(line_list[4]))
            points[line_list[1]]["count"] += 1
        except:
            points[line_list[1]] = {"diff": abs(int(line_list[3]) - int(line_list[4])), "count": 1}

for (keys, value) in points.items():
    if value["count"] >= 5:
        average_diff = value["diff"] / value["count"]
        if average_diff > highest:
            highest = average_diff
            highest_team = keys

print(highest_team, highest)  # Furman 37.833333333333336

record_file.close()

# Here, add any code you want to allow you to answer the
# questions asked below over on edX. This is just a sandbox
# for you to explore the dataset: nothing is required for
# submission here.


# QUESTION #1
# import datetime
#
# first_date = datetime.date(year=2018, month=12, day=31)
# first_team = ""
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         adate = line_list[0]
#         adate = adate.split("-")
#         adate = datetime.date(year=int(adate[0]), month=int(adate[1]), day=int(adate[2]))
#         if first_date > adate:
#             first_date = adate
#             first_team = line_list[1]
#
# print(first_date) # 1902-10-11
# print(first_team) # Auburn


# QUESTION #2 & 3
# points_for = 0
# points_against = 0
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         if line_list[1] == "Auburn":
#             points_for += int(line_list[3])
#             points_against += int(line_list[4])
#
#
#
# print(points_for) #1327
# print(points_against) #1143


# QUESTION #5
# wins = 0
# losses = 0
# ties = 0
#
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if line_list[2] == "Home":
#         if int(line_list[3]) > int(line_list[4]):
#             wins += 1
#         elif int(line_list[3]) < int(line_list[4]):
#             losses += 1
#         elif int(line_list[3]) == int(line_list[4]):
#             ties += 1
#
# print(str(wins) + "-" + str(losses) + "-" + str(ties)) # 513-226-27

# QUESTION #5
# wins = 0
# losses = 0
# ties = 0
#
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if "2009" in line_list[0]:
#         if int(line_list[3]) > int(line_list[4]):
#             wins += 1
#         elif int(line_list[3]) < int(line_list[4]):
#             losses += 1
#         elif int(line_list[3]) == int(line_list[4]):
#             ties += 1
#
# print(str(wins) + "-" + str(losses) + "-" + str(ties)) #11-3-0


# QUESTION #6
# wins = 0
# losses = 0
# ties = 0
#
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if "-10-" in line_list[0]:
#         if int(line_list[3]) > int(line_list[4]):
#             wins += 1
#         elif int(line_list[3]) < int(line_list[4]):
#             losses += 1
#         elif int(line_list[3]) == int(line_list[4]):
#             ties += 1
#
# print(str(wins) + "-" + str(losses) + "-" + str(ties)) #302-177-10

# QUESTION 7
# wins = 0
# losses = 0
# ties = 0
#
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         month_list = line_list[0].split("-")
#         if int(month_list[0]) >= 1933 and int(month_list[0]) <= 1963:
#             if int(line_list[3]) > int(line_list[4]):
#                 wins += 1
#             elif int(line_list[3]) < int(line_list[4]):
#                 losses += 1
#             elif int(line_list[3]) == int(line_list[4]):
#                 ties += 1
#
# print(str(wins) + "-" + str(losses) + "-" + str(ties)) #206-110-12

# QUESTION #8
# points = {}
# highest = 0
# highest_team = ""
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         try:
#             points[line_list[1]] += int(line_list[3])
#         except:
#             points[line_list[1]] = int(line_list[3])
#
# for (keys, value) in points.items():
#     if value > highest:
#         highest = value
#         highest_team = keys
#
# print(highest_team, highest) # Duke, 1869

# QUESTION #9
# points = {}
# zero_points_team = ""
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         try:
#             points[line_list[1]] += int(line_list[3])
#         except:
#             points[line_list[1]] = int(line_list[3])
#
# for (keys, value) in points.items():
#     if value == 0:
#         print(keys) #St. Albans / Carnegie Tech


# QUESTION #10
# points = {}
# zero_points_team = ""
# counter = 0
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         try:
#             points[line_list[1]] += int(line_list[4])
#         except:
#             points[line_list[1]] = int(line_list[4])
#
# for (keys, value) in points.items():
#     if value == 0:
#         print(keys) #
#         counter += 1
#
# Carlisle
# Fort Benning
# Camp Logan
# Camp Gordon
# Tennessee Medical
# Indiana State
# Cumberland
# Centre
# Transylvania
# North Georgia
# Elon
# 11

# QUESTION 12
# points = {}
# highest = 0
# highest_team = ""
#
# for lines in record_file:
#     lines = lines.rstrip("\n")
#     line_list = lines.split(",")
#     if not line_list[0] == "Date":
#         try:
#             points[line_list[1]] += abs(int(line_list[3]) - int(line_list[4]))
#         except:
#             points[line_list[1]] = abs(int(line_list[3]) - int(line_list[4]))
#
# for (keys, value) in points.items():
#     if value > highest:
#         highest = value
#         highest_team = keys
#
# print(highest_team, highest) # Georgia 1455
