"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.

The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

"""

#input and preprocess
m_len, m = input(), input().split()
n_len, n = input(), input().split()


def find_symmetric_difference(m, n):
    o = set(sorted([int(i) for i in m+n], reverse=True))
    
    for i in o:
        print(i)
    

if __name__ == "__main__":
    pass
