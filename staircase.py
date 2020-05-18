#https://www.hackerrank.com/challenges/staircase/problem

#print a stair case of size = n

'''
   #
  ##
 ###
####
'''
#the above is an example of n = 4, where the base = height of the staircase.

# constraints 0 < n =< 100

n = int(input())

def staircase(n):
  for i in range(n):
    string = ' ' * n
    print(string.replace(' ', '#', 1 + i)[::-1])

staircase(n)