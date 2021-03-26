# Задание 6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func():
    user_word = input('Введите слово маленькими латинскими буквами: ')
    return user_word.title()

result = int_func()

print(result)

# продолжение

def int_func2():
    user_str = input('Введите строку из слов маленькими латинскими буквами')
    for char in user_str:
        if char.isalpha():
            print((user_str.title()).split())
        else:
            print('Вводить только латинские буквы!')

result = int_func2()

print(result)