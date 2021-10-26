import datetime
import os

print(datetime.datetime.fromtimestamp(os.path.getmtime("../.gitignore")))

for cd in os.walk(os.pardir):
    for folder in cd[1]:
        print("Папка ", folder)
