import datetime

print(datetime.datetime.now())
print(datetime.date.today())


from datetime import datetime


date = datetime.now()
print(date)
print(date.strftime("%a"))
print(date.strftime("%A"))
print(date.strftime("%w"))
print(date.strftime("%d"))
print(date.strftime("%b"))
print(date.strftime("%B"))
print(date.strftime("%m"))

print(date.strftime("%a %d %b %Y %H:%M:%S %p"))


# timezone
import pytz
from datetime import datetime

time1 = pytz.timezone("Asia/Kolkata")
date = datetime.now(time1)
print(date)

time2 = pytz.timezone("US/Pacific")
date = datetime.now(time2)
print(date)


# timedelta
from datetime import timedelta

date = datetime.now()
newdate = date + timedelta(days=10, minutes=10, seconds=10)
print(newdate)


# calculate years
from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    age = today - birth_date
    age_in_years = age.days // 365.2425
    return int(age_in_years)

dob = date(2000, 1, 1)
print(calculate_age(dob))   # 26


# strptime
date_in_str = "20 August 2023"
date_obj = datetime.strptime(date_in_str, "%d %B %Y")
print(date_obj)     # 2023-08-20 00:00:00
print(date_obj.year)   # 2023
print(date_obj.month)   # 8
print(date_obj.day)     # 20





