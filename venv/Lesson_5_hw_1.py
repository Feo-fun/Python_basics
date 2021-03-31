with open('hw_1.txt', 'w', encoding='utf-8') as my_file:
    while True:
        user_info = input('Введите данные в виде строки через пробел: ')
        if not user_info:
            break
        my_file.write(f'{user_info}\n')
        print(user_info)

