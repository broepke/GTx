# -----------------------------------------------------------
# Recall in an earlier problem you were given two lists: one
# list was a student's answers to a test, and the other was
# the answer key. Your goal was to return a score
# representing the number of problems the student got correct.
#
# Let's do that again, but with dictionaries instead of lists.
# Write a function called calculate_score. calculate_score
# should take two parameters: a dictionary of student answers
# and a dictionary of correct answers. Both dictionaries should
# have integers as their keys, and one-character strings as
# their values.
#
# calculate_score should count how many questions the student
# got right. Or, in more precise terms, calculate_score should
# count how many keys for which the associated value is the
# same in the student's dictionary and in the answer key
# dictionary.
#
# As before, it is possible that there will be more answers in
# one than the other. This means that these answers don't
# belong to the same test! If that happens, return -1.


# Add your function here!
def calculate_score(student_answers, correct_answers):
    score = 0

    for questions in correct_answers.keys():
        if len(student_answers) == len(correct_answers):
            if student_answers[questions] == correct_answers[questions]:
                score += 1
        else:
            score = -1

    return score


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "B"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))
