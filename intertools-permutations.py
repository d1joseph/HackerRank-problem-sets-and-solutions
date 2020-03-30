from itertools import permutations

'''
You are given a string S. Print all posible permutations of size K of the string in lexicographic sorted order.

**input format**

Single line containing the space seperated string S and int value K

**output format**

Print the permutations of the string S.

Problem link: https://www.hackerrank.com/challenges/itertools-permutations/problem 

'''


string_int = input()

def permuta(string_int):
    string_ = []
    int_ = int(string_int[-1])
    for x in string_int.replace(' ',''):
        string_.append(x)
    del string_[-1]
        
    result = list(sorted(map("".join, permutations(string_, int_))))
    return result

for i in permuta(string_int):
    print(str(i))

#by Dhiv Joseph
