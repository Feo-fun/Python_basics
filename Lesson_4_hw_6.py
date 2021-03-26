from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числа нажмите Enter,\n'
      'для выхода нажмите "q"')

for num in count(int(input('Введите целое число: '))):
    print(num, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Для генерации следующего элемента нажмите Enter,\n'
      'Для выхода из программы нажмите "q"')

user_list = input('Создайте список, разделяя элементы пробелом: ').split()
rep_el = cycle(user_list)
quit = None

while quit != 'q':
    print(next(rep_el), end='')
    quit = input()

