# Recall Coding Problem 4.3.9 (Advanced), the free body
# diagram problem. If you were unable to solve that, we've
# included the sample answer in the dropdown in the top left
# -- feel free to use that to write your answer to this
# problem.
#
# Revise your code from that problem to use a file instead of
# a list as its parameter. Name this new function
# find_net_force_from_file. The function should take one
# parameter, the name of a file. The function should return
# the net magnitude and direction, just as it did in the other
# problem.
#
# Each line of the file will have two numbers, both integers:
# the first number will be the magnitude, and the second
# number will be the angle (in degrees, from -180 to 180).
# There will be a space between them.
#
# HINT: You may have multiple functions in your code if you
# want!
#
# HINT 2: Try to write this such that you can reuse as much
# of your earlier code as possible. Remember, when loading
# from a file, any text you load is initially a string. You'll
# almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt


# Add your function here!
def find_net_force_from_file(a_file):
    total_horizontal = 0
    total_vertical = 0
    a_list = []
    b_list = ()

    my_file = open(a_file, "r")

    # forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
    for line in my_file:
        b_list = (line.split())
        b_list[0] = int(b_list[0])
        b_list[1] = int(b_list[1])
        a_list.append(b_list)

    # sum the total horizontal and vertical forces
    for i in a_list:
        total_horizontal = total_horizontal + (i[0] * cos(radians(i[1])))
        total_vertical = total_vertical + (i[0] * sin(radians(i[1])))

    # - Use the Pythagorean theorem to calculate the total
    total_magnitude = sqrt(total_horizontal ** 2 + total_vertical ** 2)

    # - Use inverse tangent to calculate the angle:
    fin_angle = atan2(total_vertical, total_horizontal)
    fin_angle = degrees(fin_angle)

    answer = (round(total_magnitude, 1), round(fin_angle, 1))

    my_file.close()

    return answer


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
