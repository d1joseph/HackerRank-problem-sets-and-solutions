"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.

The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

"""

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

if __name__ == "__main__":
    pass
