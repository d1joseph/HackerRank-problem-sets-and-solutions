"""
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
"""

import numpy as np

#---------- reference ----------

#zero tool float and int - outputs [[0. 0.]] [[0 0]]
#zero_tool_float = np.zeros((3,3,3))

#zero_tool_int = np.zeros((1,2), dtype = np.int)

#ones tool float and int - outputs [[1. 1.]] [[1 1]]
#ones_tool_float = np.ones((1,2))

#ones_tool_int = np.ones((1,2), dtype = np.int)

#---------- solution ----------

#pass the input into the the zero_tool_int and ones_tool_int in the required format.
#call the function to output the array


#function to convert the format from space seperated integers into comma deliminated.

space_value = '3 3 3'

import numpy as np

space_value = input()

def solution_zeroes(space_value):
        space_value_n = list(map(int, space_value.split()))
        zero_tool_int = np.zeros((space_value_n), dtype = np.int)
        return zero_tool_int

def solution_ones(space_value):
    space_value_n = list(map(int, space_value.split()))
    ones_tool_int = np.ones((space_value_n), dtype = np.int)
    return ones_tool_int

print(solution_zeroes(space_value))
print(solution_ones(space_value))
