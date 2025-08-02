import datetime

temp_y = datetime.datetime.now().year
temp_m = datetime.datetime.now().month
temp_d = datetime.datetime.now().day

print(temp_y)
print(temp_m)
print(temp_d)

# Custom datetime
custom_date = datetime.datetime(2025, 3, 1, 12, 22)
print(custom_date)

# Format datetime
today = datetime.datetime.now()
formatted_date_1 = today.strftime("%Y/%m/%d")
formatted_date_2 = today.strftime("%Y/%m/%d %H:%M:%S")
formatted_date_3 = today.strftime("%d,%B,%m %H:%M:%S")

print(formatted_date_1)
print(formatted_date_2)
print(formatted_date_3)
print(type(formatted_date_3))

# datetime string to datetime object
date_str = "23,Feb,2025 - Sun 09:08:44 PM"
datetime_obj = datetime.datetime.strptime(date_str, "%d,%b,%Y - %a %I:%M:%S %p")
print(datetime_obj)


#date time minus
# Date Arithmatic
from datetime import timedelta, datetime
today= datetime.today()
tomorrow = today + timedelta(days=1)
previous= today - timedelta(days=1)
print(today)
print(tomorrow)
print(previous)

abir_born = datetime.strptime("16 Nov 2001", "%d %b %Y")
abir_age= today- abir_born
print(abir_age)
