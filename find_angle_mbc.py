'''
You are given the lengths AB and BC.

Your task is to find the midpoint of the hypotenuse, MBC, (angle 0 degrees , as shown in the figure) in degrees.

Input format

- The first line contains the length of side AB.
- The second line contains the length of side BC.

Output format

- output the angle of MBC in degrees. Round to the nearest integer.

'''

import math

AB,BC = int(input()),int(input())

def find_angle_MBC(AB, AC):
    MBC = math.degrees(math.atan2(AB,BC))
    return MBC

print(str(int(round(find_angle_MBC(AB, BC))))+ '°')
