# Basketball coach Phil Jackson says that in order for an NBA
# team to be a contender for a championship, they need to win
# 40 games before they lose 20 games.
#
# Write a function called is_a_contender that will take three
# parameters: a team name (a string), a number of wins (an
# integer), and a number of losses (an integer).
#
# Based on these parameters, the function should return one
# of three strings:
#
# - If the team is a contender (at least 40 wins and fewer
#   than 20 losses), return "The [team name] are a contender!"
# - If the team is not a contender (less than 40 wins and at least
#   20 losses), return "The [team name] are not a contender!"
# - If it cannot be determined (both values are higher or both
#   values are lower), return "The [team name] might be a contender!"


# Add your code here!
def is_a_contender(name, wins, losses):
    if wins >= 40 and losses <= 20:
        return "The " + name + " are a contender!"
    elif wins < 40 and losses >= 20:
        return "The " + name + " are not a contender!"
    else:
        return "The " + name + " might be a contender!"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: "The Hawks are not a contender!".

test_team_name = "Hawks"
test_wins = 18
test_losses = 40

print(is_a_contender(test_team_name, test_wins, test_losses))
