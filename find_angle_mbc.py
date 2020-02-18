'''
You are given the lengths AB and BC.

Your task is to find the midpoint of the hypotenuse, MBC, (angle 0 degrees , as shown in the figure) in degrees.

Input format

- The first line contains the length of side AB.
- The second line contains the length of side BC.

Output format

- output the angle of MBC in degrees. Round to the nearest integer.

'''
from math import sqrt as sq

#Lengths
AB = float(input('Enter length of side AB: '))
BC = float(input('Enter length of side BC: '))

#finds the length of side AC when given AB and BC as parameters.
def pythagoras_T(AB,BC):
    AC = int(sq(AB**2 + BC**2))
    return 'AC length is ' + str(AC)

print(pythagoras_T(AB,BC))
