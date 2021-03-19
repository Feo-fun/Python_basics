# Задание 1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return 'Value Error!'
    except ZeroDivisionError:
        return 'You cannot divide by zero!!'
    return div_num

print(div(input('Enter number: '), input('Enter number: ')))
