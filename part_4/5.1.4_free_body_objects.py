# Recall in Coding Problem 4.4.4 (and before that, in Coding
# Problem 4.3.9) you built a program for finding the net
# force (magnitude and angle) on an object from several
# individual forces.
#
# In the next two exercises, we're going to convert that
# system into one that uses objects.
#
# To start, create a class called Force. The constructor for
# Force should have two required arguments: magnitude and
# angle. These should be saved to two attributes called
# 'magnitude' and 'angle'. You should assume angle is
# initially in degrees, from -180 to 180.
#
# Then, add three methods to Force:
#
# - get_horizontal should return the horizontal component
#   of the force, according to the formula:
#   horizontal = magnitude * cos(angle).
# - get_vertical should return the vertical component of
#   the force, according to the formula:
#   vertical = magnitude * sin(angle).
# - get_angle should return the angle of the force, but
#   should have a keyword parameter called use_degrees.
#   use_degrees should default to True. If use_degrees
#   is true, it should return the angle in degrees; if it
#   is false, it should return the angle in radians.
#
# HINT: Don't overcomplicate this. All we want here is
# a class called Force with four methods: __init__,
# get_horizontal, get_vertical, and get_angle. Note that
# these are not true "getters" even though they have "get"
# in their names: all three will have some reasoning
# beyond just returning a single value.
#
# HINT 2: angle will initially be passed into the
# constructor in degrees. You may store it in either
# degrees or radians. Each approach has different benefits,
# but make sure to keep track of when it's in angles and
# when it's in degrees.

from math import sin, cos, atan2, radians, degrees, sqrt

# Add your code here!
class Force:
    def __init__(self, magnitude ,angle):
        self.magnitude = magnitude
        self.angle = angle
        self.horizontal = 0
        self.vertical = 0

    def get_horizontal(self):
        self.horizontal = self.magnitude * cos(radians(self.angle))
        return self.horizontal

    def get_vertical(self):
        self.vertical = self.magnitude * sin(radians(self.angle))
        return self.vertical

    def get_angle(self, use_degrees=True):
        if not use_degrees:
            return atan2(self.vertical, self.horizontal)
        else:
            return degrees(atan2(self.vertical, self.horizontal))



# Below are some lines of code that will test your object.
# You can change these lines to test your code in different
# ways.
#
# If your code works correctly, this will originally run
# error-free and print (with room for rounding errors):
# Magnitude: 500
# Horizontal: 250.0
# Vertical: 433.0127018922193
# Angle in Degrees: 60.0
# Angle in Radians: 1.0471975511965976
a_force = Force(500, 60)
print("Magnitude:", a_force.magnitude)
print("Horizontal:", a_force.get_horizontal())
print("Vertical:", a_force.get_vertical())
print("Angle in Degrees:", a_force.get_angle())
print("Angle in Radians:", a_force.get_angle(use_degrees=False))
