"""
Write a Python program which creates a random date. HINT: use the datetime and random modules
"""

import random
import datetime

start_dt = datetime.date(2019, 1, 1)
end_dt = datetime.date(2022, 12, 31)

time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days

random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)
print(random_date)



