# !/usr/bin/python
# -*- coding: utf-8 -*-
import math


class Point:
    """Represents a point in two-dimensional geometric coordinates"""

    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the point
        defaults to the origin
        """
        self.move(x, y)

    def move(self, x, y):
        """Move the point to a new location in two-dimensional space."""
        self.x = x
        self.y = y

    def reset(self):
        """Reset the point to a new location in two-dimensional space"""
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point
        passed as a parameter"""
        return math.sqrt((self.x - other_point.x) ** 2
                         + (self.y - other_point.y) ** 2)


p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)

p1.reset()
print(p1.x, p1.y)

p2.move(5, 0)
print(p2.calculate_distance(p1))
assert (p2.calculate_distance(p1) == p1.calculate_distance(p2))
p1.move(3, 4)
print("{:f}".format(p1.calculate_distance(p2)))
print(p1.calculate_distance(p1))
