"""
8. Write a Python program which prints the next 5 days starting from today.
"""
import datetime

start_dt = datetime.date.today()

i = 0
while i <= 4:
    i += 1
    next_5_days_are = start_dt + datetime.timedelta(days=i)
    print(next_5_days_are)
