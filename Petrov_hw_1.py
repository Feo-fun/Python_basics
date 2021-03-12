# Задание 1 (поработать с переменными: строки, числа)
user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))

print(user_name)
print(user_age)

# Задание 2 (перевести время в секундах в формат чч:мм:сс)
user_time = int(input('Введите время в секундах: '))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time - (hours * 3600 + minutes * 60)
print(f'чч:мм:сс {hours}:{minutes}:{seconds}')

# Задание 3
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_number = int(input('Введите число: '))
total_number = (user_number + int(str(user_number) + str(user_number)) + int(str(user_number) + str(user_number) + str(user_number)))
print(f'Сумма чисел n + nn + nnn = {total_number}')


# Задание 4 (найти максимальное значение в целом числе)
user_number = abs(int(input("Введите целое число: ")))

max_number = 0

while user_number > 0: # True or False
    item = user_number % 10 # 42 % 10 = 2
    if item >= max_number:
        max_number = item

    user_number = user_number // 10 # 42 // 10 = 4

print(max_number)

# Задание 5 (выручка и прибыль)
profit = float(input('Укажите сумму выручки компании: '))
costs = float(input('Укажите сумму издержек компании: '))
if profit > costs:
    print(f'Компания работает с прибылью. Рентабельность выручки составила {profit / costs}')
    workers = int(input('Введите количество сотрудников компании: '))
    print(f'Размер прибыли в расчёте на одного сотрудника составляет {(profit - costs) / workers}')
elif profit == costs:
    print('Компания вышла в ноль')
else:
    print('Компания работает в убыток')

# Задание 6 (Спортсмен занимается бегом)

a = int(input('Сколько километров вы пробежали в первый день? '))
b = int(input('Какой ваш желаемый результат в км? '))

days_to_goal = 1
km_to_goal = a
while km_to_goal < b:
    a = a + a * 0.1
    days_to_goal +=1
    km_to_goal = int(km_to_goal + a)
print(f'Вы достигнете своей цели на {km_to_goal} день')


