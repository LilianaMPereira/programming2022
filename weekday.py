"""
Weekly Task 05
Write a program that outputs whether or not today is a weekday.

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!
"""
# This task is the Weekly Task 05
# This program shows the outputs whether or not today is a weekday. 
# Information about Python Program how to get the day of a week given: https://www.hellocodeclub.com/python-get-day-of-week/ ; https://www.sanfoundry.com/python-https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/ ; https://pythontic.com/datetime/date/weekday ; https://www.youtube.com/watch?v=qMrUkDHS_cA

from datetime import date
import calendar
curr_date = date.today()

today = calendar.day_name[curr_date.weekday()]

print("Today is", today)

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursady', 'Friday']

if today in weekday:
    print("Yes, unfortunately today is a Weekday!")
else:
    print("Weekend!")
