# Задание 1 (создать список с разными типами данных)

my_list = ['Дионисий', 28, 79.8, None, True, 'врач']

for el in my_list:
    print(type(el))
# на момент выполнения задания мы еще не имели представления о функциях def. Без гугла и просмотра следующего занятия
# невозможно было догадаться о выполнении этого задания через def. И нужно ли? Если через for in нормально проверяет.
# прокомментируйте на уроке, пожалуйста!
# в гугле вот такой вариант решения:
# def my_type(i):
#     for i in range(len(my_list)):
#         print(type(my_list[i]))
#     return
#
# my_type(my_list)

# Задание 2 (Обмен значений соседних элементов)
item_count = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
el = 0
while i < item_count:
    my_list.append(input("Введите следующее значение списка: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
#

# Задание 3 (определить сезон года по номеру месяца)
#
season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

month = int(input('Введите номер месяца: '))

if month == 12 or month == 1 or month == 2:
    print(season_dict.get(1))
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(4))
    print(season_list[3])
else:
    print('Неверное значение месяца!')

# Задание 4 (Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки, пронумеровать).
my_string = input('Расшифруйте аббревиатуру "СССР": ')

new_list = list(my_string.split(' '))
number = 1
for number, word in enumerate(new_list, 1):
    if len(word) <=10:
        print(number, word)
    else:
        print(number, word[:10])
    number += 1

# Задание 5 (структура "Рейтинг")

rating = [14, 11, 8, 8, 6, 3, 1]
print(f'Рейтинг: {rating}')
new_score = int(input('Введите новое значение рейтинга: '))

while new_score <= 100:
    for score in range(len(rating)):
        if rating[score] == new_score:
            rating.insert(score + 1, new_score)
            break
        elif rating[0] < new_score:
            rating.insert(0, new_score)
        elif rating[-1] > new_score:
            rating.append(new_score)
        elif rating[score] > new_score and rating[score + 1] < new_score:
            rating.insert(score + 1, new_score)
    print(rating)
    break

# Задание 6


product_list = []
product_dict = []
analytics_dict = {}
i = 1

while True:
    product_dict = dict({'Название': str(input('Введите название товара: ')),
                         'цена': float(input('Введите цену на товар: ')),
                         'количество': int(input('Введите кол-во товара: ')),
                         'единицы': str(input('Введите единицы измерения: '))})
    product_list.append((input('Введите порядковый номер товара: '), product_dict))
    i += 1
    if input('Добавить информацию о ещё одном товаре? ') != 'да':
        break

    analytics_dict = dict({'название': product_dict.get('название'), 'цена': product_dict.get('цена'), 'количество': product_dict.get('количество'), 'единицы': product_dict.get('единицы')})

print(f'Список товаров: {product_list}')
print(f'Товары по категориям: {analytics_dict}')


