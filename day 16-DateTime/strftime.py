from datetime import datetime

#strftime

# Python strftime cheatsheet-  https://strftime.org/

now= datetime.now()
print(now)
t= now.strftime("%H:%M:%S")
print("time: ",t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)