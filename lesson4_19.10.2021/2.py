current_max_age = 120
current_min_age = 0
supposed_age = current_max_age
count = 0
supposed_ages = []

while True:
    count += 1
    supposed_ages.append(supposed_age)
    answer = input(
        f'Вам {supposed_age} лет? Если меньше, то введите знак "<", инача ">": ')
    if answer == "Да":
        print(f"Вам {supposed_age}! Угадал за {count} итераций")
        break
    elif answer == "<":
        current_max_age = supposed_age
        supposed_age = (current_max_age - current_min_age) // 2 + current_min_age
    elif answer == ">":
        current_min_age = supposed_age
        supposed_age = (current_max_age - current_min_age) // 2 + current_min_age
    else:
        count -= 1
        print("Введите корректное значение!")
    if supposed_age in supposed_ages:
        print("Ах ты хитрый татарин!")
        break

