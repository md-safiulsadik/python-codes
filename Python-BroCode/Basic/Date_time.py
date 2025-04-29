
import datetime

date = datetime.date(year=2024, month=5,day=12)

today = datetime.date.today()

time = datetime.time(hour=5, minute=54, second=55)

time_now = datetime.datetime.now().strftime("%H:%M:%S  %d-%m-%Y")

target_datetime = datetime.datetime(year=2023, month=12, day=4)
now = datetime.datetime.now()

# print(time_now)

if target_datetime < now:
    print("You have time")
else:
    print("You don't have time")