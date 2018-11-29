rating = "R"
age = 15

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# The United States has a movie rating system that rates
# movies with one of five ratings: G, PG, PG-13, R, and NC-17.
# Although some of the ratings are not binding, imagine that
# you are a parent who decides on the following rules:
#
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#
# The variables above give a rating and a child's age. Use
# these variables to select and print one of these two
# messages based on the criteria above:
#
# - "You may see that movie!"
# - "You may not see that movie!"
#
# However, there's one trick: you may not use the 'and' operator
# anywhere in this code!


# Add your code here!
can_go = False

if rating == "R":
    rating = 4
elif rating == "PG-13":
    rating = 3
elif rating == "PG":
    rating = 2
elif rating == "G":
    rating = 1
else:
    rating = 10

if rating == "NC-17":
    can_go = False
elif age < 8:  # G Rated
    if rating == 1:
        can_go = True
elif age < 13:  # PG Rated
    if rating <= 2:
        can_go = True
elif age < 17:  # PG-13 Rated
    if rating <= 3:
        can_go = True
elif age >= 17:
    if rating <= 4:
        can_go = True
else:
    can_go = False

if can_go:
    print("You may see that movie!")
else:
    print("You may not see that movie!")
