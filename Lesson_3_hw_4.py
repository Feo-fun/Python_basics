# Задание 4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
def my_func(x, y):
    result = x ** y
    return result

result = my_func(int(input('Введите действительное положительное число: ')),
                 int(input('Введите целое отрицательное число: ')))

print(result)

def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'x должно быть > 0, y должно быть < 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения числа x в степень y: {result}'
    except ValueError:
        return 'Вводить только числа!'

num_1 = input('Введите действительное положительное число: ')
num_2 = input('Введите целое отрицательное число: ')

print(my_func2(num_1, num_2))