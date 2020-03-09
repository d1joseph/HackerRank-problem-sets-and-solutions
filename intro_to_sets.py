'''
Calculate the average of the array using only the distinct values of the set.

***Input***

Line 1 contains the integer, N, the total elements in the array.
Line 2 contains the N space seperated elements of the array.

'''

def average(arr):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
