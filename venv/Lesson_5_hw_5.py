from random import randint

with open('text_5.txt', 'w', encoding='utf-8') as num_file:
    num_list = [randint(1, 1000) for _ in range(100)]
    num_file.write(" ".join(map(str, num_list)))

print(f'Сумма элементов - {sum(num_list)}')
