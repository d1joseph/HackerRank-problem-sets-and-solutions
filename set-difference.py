# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# my solve for ^

# Enter your code here. Read input from STDIN. Print output to STDOUT

# process STDIN
a_count, a = input(), input()
b_count, b = input(), input()

a_set = set(a.split(' '))
b_set = set(b.split(' '))

# solution
def set_difference(a,b):
    return len(a.difference(b))


if __name__ == "__main__":
    print(set_difference(a_set,b_set))