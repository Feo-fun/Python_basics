# Задание 3

# def my_func(num_1, num_2, num_3):
#     sum = max(num_1, num_2) + max(num_2, num_3)
#     return sum
#
#
# print(my_func(int(input('Введите аргумент: ')), int(input('Введите аргумент: ')), int(input('Введите аргумент: '))))
#
#
def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Вводить только числа!'


print(my_func(int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))))

# my_func = lambda num_1, num_2, num_3: (num_1 + num_2 + num_3) - min(num_1, num_2, num_3)
#
#
# print(my_func(23, 567, 235))