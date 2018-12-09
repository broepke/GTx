# In this problem, we're giving you a file containing some real data from
# the Marta (Atlanta's subway system) database. Each line of the file is
# a record of a single ride at a specific Marta station. Riders enter and
# exit the subway system by tapping a Breeze Card against a gate at a
# specific station.
#
# You can see a preview of what the file will look like in
# marta_sample.csv in the dropdown in the top left. Note, however, that
# the real dataset is massive: over 200,000 individual rides are recorded.
# So, you're going to be dealing with some pretty big data!
#
# Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
# Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
# Note that you will answer these questions in the fill-in-the-blank
# problems below, _not_ in this coding exercise. So, you don't have to
# programmatically find the station ID closest to the average: you could
# just print all the stations and their averages, then visually check
# which is closest to the average.
#
# To get you started, we've gone ahead and opened the file:

# marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')

marta_file = open("marta_sample.csv", "r")

# Start by building out the dictionary of the total taps per station
station_taps = {}

for lines in marta_file:
    line = lines.split(",")
    if line[3] in station_taps.keys():
        station_taps[line[3]] += 1
    else:
        station_taps[line[3]] = line[3]
        station_taps[line[3]] = 1

print(station_taps)

# What is the average number of Breeze Card taps per station?
total = 0
counter = 0
for stops in station_taps.values():
    total += stops
    counter += 1

stops_avg = total / counter

print("\nAverage stops", stops_avg)

# What is the station ID of the station whose traffic is the closest to that average?
delta = 100000
current_closest_station = ""

for (stations, taps) in station_taps.items():
    station_delta = taps - stops_avg
    station_delta = station_delta.__abs__()
    if station_delta < delta:
        delta = station_delta
        current_closest_station = stations

print("\nCurrent Closest Station: ", current_closest_station)

# What station has the least overall amount of traffic?
least = 10000
least_station = 0
for (stations, vals) in station_taps.items():
    if int(vals) < least:
        least = int(vals)
        least_station = stations

print("\nStation with Least Taps", least_station)

# Close out the files
marta_file.close()

# You may add whatever code you want from here on to answer those three
# questions.
#
# HINT: although there are six items on each line of the file, you only
# need one of them: station ID. If you use split(",") to split up each
# line, station ID will be at index 3 on the list.
#
# HINT 2: You'll probably want to use a dictionary, with station IDs as
# the keys and