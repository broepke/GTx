# A common problem in academic settings is plagiarism
# detection. Fortunately, software can make this pretty easy!
#
# In this problem, you'll be given two files with text in
# them. Write a function called check_plagiarism with two
# parameters, each representing a filename. The function
# should find if there are any instances of 5 or more
# consecutive words appearing in both files. If there are,
# return the longest such string of words (in terms of number
# of words, not length of the string). If there are not,
# return the boolean False.
#
# For simplicity, the files will be lower-case text and spaces
# only: there will be no punctuation, upper-case text, or
# line breaks.
#
# We've given you three files to experiment with. file_1.txt
# and file_2.txt share a series of 5 words: we would expect
# check_plagiarism("file_1.txt", "file_2.txt") to return the
# string "if i go crazy then". file_1.txt and file_3.txt
# share two series of 5 words, and one series of 11 words:
# we would expect check_plagiarism("file_1.txt", "file_3.txt")
# to return the string "i left my body lying somewhere in the
# sands of time". file_2.txt and file_3.txt do not share any
# text, so we would expect check_plagiarism("file_2.txt",
# "file_3.txt") to return the boolean False.
#
# Be careful: there are a lot of ways to do this problem, but
# some would be massively time- or memory-intensive. If you
# get a MemoryError, it means that your solution requires
# storing too much in memory for the code to ever run to
# completion. If you get a message that says "KILLED", it
# means your solution takes too long to run.


# Add your code here!
def check_plagiarism(file1, file2):
    file1 = open(file1, "r")
    file2 = open(file2, "r")

    file1_str = file1.read()
    file2_list = file2.read().split()
    biggest_string_index = 5
    biggest_string = ""


    for i in range(len(file2_list)-4):
        check_string = file2_list[i] + " " + file2_list[i + 1] + " " + file2_list[i + 2] + " " + file2_list[i + 3] + " " + file2_list[i + 4]
        if file1_str.find(check_string) > 0:
            if biggest_string == "":
                biggest_string = check_string
            for j in range(len(file2_list)):
                try:
                    check_string = check_string + " " + file2_list[i+5+j]
                    if file1_str.find(check_string) > 0:
                        if biggest_string_index < i+5+j:
                            biggest_string = check_string
                            biggest_string_index = i+5+j
                    else:
                        break
                except:
                    j += 1

    file1.close()
    file2.close()

    if biggest_string == "":
        biggest_string = False

    return biggest_string


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# if i go crazy then
# i left my body lying somewhere in the sands of time
# False
# print(check_plagiarism("file_1.txt", "file_2.txt"))
# print(check_plagiarism("file_1.txt", "file_3.txt"))
# print(check_plagiarism("file_2.txt", "file_3.txt"))
print(check_plagiarism("file_qeljHc.txt", "file_xIFnml.txt"))


# "yawn catalytic prepare pneumatic mo corroboree euler tetanus reservation octoroon".
# "catalytic prepare pneumatic mo corroboree euler tetanus reservation octoroon".