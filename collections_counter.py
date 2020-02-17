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

from collections import Counter as c
import random as r
import sys



total_shoes = int(input('How many shoes do you need?: '))
total_customers = int(input('How many customers checking out?: '))
order_list = []
shoe_sizes = []

i = 0
while i <= total_customers:
    order_list.append(int(input('Customer '+ str(i) + ' selected size?: ')))
    i += 1

def make_shoes(total_shoes):
    for x in range(total_shoes):
        shoe_sizes.append(r.randint(0,16))


def check_out(total_customers):
    shoes_available = make_shoes(total_shoes)
    cost = 0


print(order_list)
