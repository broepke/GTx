# Write a function called write_1301 which will write a file
# in the format described in Coding Problem 4.4.2. The
# sample.cs1301 file has been included to refresh your
# memory. Your function should accept two arguments:
# A string of a filename to write to, and a list of tuples.
# You can assume that each tuple will have the following
# format:
#
# (int, str, int, int, float)
#
# Each tuple will represent a line in the file, and each
# item in the tuple should correspond to the
# assignment number, the assignment name, the student's
# grade, the total possible number of points, and the
# assignment weight respectively.


# Write your function here!
def write_1301(output_file, tuple_list):
    string_to_write = ""
    output_file = open(output_file, "w")

    for tuples in tuple_list:
        for i in tuples:
            string_to_write = string_to_write + str(i) + " "

        string_to_write = string_to_write.strip()
        string_to_write += "\n"


        output_file.writelines(string_to_write)
        string_to_write = ""

    output_file.close()
    return


# The code below will test your function. It's not used
# for grading, so feel free to modify it! You may check
# output.cs1301 to see how it worked.
tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("output.cs1301", tupleList)
