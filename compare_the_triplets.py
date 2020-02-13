"""
Alice and Bob each created one problem for HackerRank.

A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories:
problem clarity, originality, and difficulty.

"""

import math
import os
import random
import re
import sys

a = [1,3,5]
b = [1,4,10]

def compareTriplets(a,b):
    bob_score = 0
    alice_score = 0
    total_scores = {"alice_score": 0, "bob_score": 0}

    for i in range(len(a)):
        for j  in range(len(b)):
            if a[i] > b[j]:
                bob_score += 1
                total_scores["bob_score"] = bob_score
            elif a[i] < b[j]:
                alice_score += 1
                total_scores["alice_score"] = alice_score

    return list(total_scores.values())

print(compareTriplets(a,b))
