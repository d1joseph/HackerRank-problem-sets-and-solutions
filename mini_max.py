#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min,max = sum(arr) - sorted_arr[-1], sum(arr) - sorted_arr[0]
    print(str(min) + " " + str(max))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)