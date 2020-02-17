"""collections are containers that store array elements as dict keys and their
count as the value. """

#this challenge is a pseudo inventory check and price summary for a retail store.

"""
Task

Your client is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop.

There are N number of customers who are willing to pay Y amount of money only if they get the shoe of their desired size.

Your task is to compute how much money your client has earned.
"""

#input format
#line 1 contains X number of shoes
#line 2 contains a space seperated list of the shoe sizes
#line 3 contains the number of customers
#The next N line contains the space seperated values of the customer's desired shoe size and the Y price of that shoe.

#output format
#print the total amount earned (calculated as a function of N number of lines following the first 3 parameters.)

import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print (income)
