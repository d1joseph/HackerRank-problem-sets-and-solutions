"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.

The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

"""

<<<<<<< HEAD
#input
m_len = input()
m = list(map(int, input().split()))
m_set = set(m)
n_len = input()
n = list(map(int, input().split()))
n_set = set(n)
symm_diff = []

for i in m+n:
    if not m_set.intersection(n_set):
        symm_diff.append(i)
=======
#input and preprocess
m_len, m = input(), set(input().split())
n_len, n = input(), set(input().split())

# convert sets to list of difference values from m and n
o, p = list(n.difference(m)), list(m.difference(n))
q = [int(i) for i in o+p] # convert values to integers

# sort list and print each value
for i in sorted(q): 
    print(i)
>>>>>>> e4f93b218e97781c5d28e592fb90be9d8d72c59f

if __name__ == "__main__":
    pass
