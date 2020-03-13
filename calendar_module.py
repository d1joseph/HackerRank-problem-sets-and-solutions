
'''
You are given a date. Your task is to find what the day is on that date.

*INPUT FORMAT*

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

*OUTPUT FORMAT*

Output the correct day in capital letters.

'''

from datetime import date
import calendar

date = input()

def get_day(date):
    mmddyy = [s.lstrip('0') for s in date.split()]
    date_input = [int(a) for a in list(mmddyy)]
    calendar_day = calendar.weekday(date_input[2],date_input[0],date_input[1])
    return calendar.day_name[calendar_day].upper()

print(get_day(date))