import datetime
import random

# 1 января 1970 года
import time

start = datetime.datetime.now()

lst = [random.randint(0, 100_000) for _ in range(1_000_000)]

print(time.strftime("%H:%M:%S - %d.%m.%Y, %B"))

print(time.strptime("17:23:55 - 26.10.2021", "%H:%M:%S - %d.%m.%Y"))

print((datetime.datetime.now() - start))
