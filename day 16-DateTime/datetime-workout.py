from datetime import date, time, datetime

# print(datetime)
# print(dir(datetime))

now= datetime.now()
print(now)
day= now.day
month= now.month
year= now.year
hour= now.hour
minute= now.minute
second= now.second
timestamp= now.timestamp
# print(timestamp())

#formating
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}")


