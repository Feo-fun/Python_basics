my_dict = {}

with open('text_6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        name, data = line.split(':')
        sum_hour = sum(map(int, "".join([i for i in data if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = sum_hour

print(f'{my_dict}')

import math