start_hour = 3
start_minute = 48
length = 172

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Let's try something trickier! The variables above represent
# the start time for a run as well as the length of the run
# in minutes. The original values, for example, show a run
# that started at 3:48 and lasted 172 minutes.
#
# Add some code below that will print the time at which the
# run will end, using normal formatting (e.g. 6:40 for the
# original data above). To do this, you'll need to somehow
# find both the hours and minutes of the new time, convert
# both to strings, and add those to the colon ":" to print
# the time.
#
# You may assume that the length of the run will never cross
# 12:59 (e.g. you don't have to worry about going from
# 12:59 to 1:00 or 23:59 to 0:00). You also don't need to
# worry about the lack of 0 in front of single-digit minute
# counts (e.g. it's fine to show 5:07 as 5:7).


# Add your code here!
from datetime import datetime
from datetime import timedelta

# make a string of the start time
start_time_str = str(start_hour) + ":" + str(start_minute)

# convert that string into a datetime object
start_time = datetime.strptime(start_time_str, "%H:%M")

finish_time = start_time + timedelta(minutes=length)

print(str(finish_time.hour) + ":" + str(finish_time.minute))
