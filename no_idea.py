'''
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in Set B.

Your initial happiness is 0. 

For each i integer in array. of i == A, you add 1 to happiness. 

If i == B, you minus 1 from happiness.

Output your final happiness. Note your happiness can have a negative index range.

'''


n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())

def intersect(array, A, B):
    happiness = sum([(i in A) - (i in B) for i in array])
    return happiness

print(intersect(array,A,B))