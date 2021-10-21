timetable = {
    "Понедельник": {
        "11:00": "Завтрак",
        "12:00": "Математический анализ",
        "13:40": "Алгем",
    },
    "Вторник": {
        "11:00": "Завтрак",
        "12:00": "Матан",
        "13:40": "Алгем",
    }, "Среда": {
        "11:00": "Завтрак",
        "12:00": "Матан",
        "13:40": "Алгем",
    }, "Четверг": {
        "11:00": "Завтрак",
        "12:00": "Матан",
        "13:40": "Алгем",
    }, "Пятница": {
        "11:00": "Завтрак",
        "12:00": "Матан",
        "13:40": "Алгем",
    }, "Суббота": {
        "11:00": "Завтрак",
        "12:00": "Матан",
        "13:40": "Алгем",
    },
}

max_day_len = 0
max_task_len = 0
for day in timetable:
    max_day_len = max(max_day_len, len(day))
    for task in timetable[day].values():
        max_task_len = max(max_task_len, len(task))

print(max_day_len, max_task_len)

for day in timetable:
    print("-" * (max_task_len + 13))
    print("|", day.rjust((max_task_len + 13 - len(day)//2) // 2).ljust(
        (max_task_len + 13) - len(day)), "|")
    print("-" * (max_task_len + 13))
    for time, task in timetable[day].items():
        print(f"| {time} {task.rjust(max_task_len)} |")
    print()



