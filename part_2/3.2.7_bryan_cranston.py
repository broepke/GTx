story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# In Bryan Cranston's autobiography, he describes how after
# his success on Breaking Bad, he developed a scoring system
# for evaluating new scripts that he received.
#
# First, he would assign the script a grade -- A, B, C, D, or
# F -- in each of five categories: Story, Text, Role, Director,
# and Cast.
#
# Then, he would tally those grades into a total score for the
# script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
# For example: an A story, B text, C role, D directory, and
# F cast would get a score of 12: +6 for the story, +4 for the
# text, +2 for the role, +0 for the director, and +0 for the
# cast.
#
# Then, based on that score, the script would be assigned a
# category (note these are slightly different from the image
# because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
# The variables above give the letter grades assigned to each
# of the five components. Write a program that calculates the
# total score he would assign to the script represented by
# these variables. Then on the next line, print the category
# he would assign to that script. For example, for the values
# above, this program would print:
#
# 12
# Pass
#
# HINT: This is a *long* program. It's not particularly
# complex -- you're doing the same thing over and over, However,
# that 'same thing' required 4-8 lines each time you do it. Our
# answer is 46 lines long! So, don't think you're off-track just
# because you're writing a lot of lines.


# Add your code here!
total = 0
category = ""

# Story
if story == "A":
    total += 6
elif story == "B":
    total += 5
elif story == "C":
    total += 4
elif story == "D":
    total += 2

# Text
if text == "A":
    total += 5
elif text == "B":
    total += 4
elif text == "C":
    total += 3
elif text == "D":
    total += 1

# Role
if role == "A":
    total += 4
elif role == "B":
    total += 3
elif role == "C":
    total += 2
elif role == "D":
    total += 1

# Director
if director == "A":
    total += 3
elif director == "B":
    total += 2
elif director == "C":
    total += 1

# Cast
if cast == "A":
    total += 2
elif cast == "B":
    total += 1

if total == 20:
    category = "Perfect score"
elif 17 <= total <= 19:
    category = "Must do"
elif 14 <= total <= 16:
    category = "Seriously consider"
elif 12 <= total <= 13:
    category = "On the bubble"
else:
    category = "Pass"

print(total)
print(category)
