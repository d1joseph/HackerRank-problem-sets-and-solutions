n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())

def intersect(array, A, B):
    happiness = sum([(i in A) - (i in B) for i in array])
    return happiness

print(intersect(array,A,B))