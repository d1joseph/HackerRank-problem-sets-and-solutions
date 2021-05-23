# hackerrank problem - set.unions()
# problem - https://www.hackerrank.com/challenges/py-set-union/problem

# comments - this test should be review. The 1st and 3rd input isn't required to solve the problem.
# total_a_students and total_b_students variables I've declared below are just to get around HCs input requirements 


total_a_students, a_students = input(), input().split()
total_b_students, b_students = input(), input().split()

c_students = set(a_students).union(set(b_students))

# print(len(c_students))
