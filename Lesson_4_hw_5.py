from functools import reduce

def my_func(num_1, num_2):
    return num_1 * num_2


my_list = [num for num in range(100, 1001, 2)]

print(f'Исходный список: \n{my_list}\nПроизведение всех чисел из списка: \n{reduce(my_func, my_list)}')

