"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.

The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

"""

#input and preprocess
m_len, m = input(), set(input().split())
n_len, n = input(), set(input().split())

# convert sets to list of difference values from m and n
o, p = list(n.difference(m)), list(m.difference(n))
q = [int(i) for i in o+p] # convert values to integers

# sort list and print each value
for i in sorted(q): 
    print(i)

if __name__ == "__main__":
    pass
