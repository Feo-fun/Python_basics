import json

with open('text_7_new.json', 'w', encoding='utf-8') as new_file:
    with open('text_7.txt', 'r', encoding='utf-8') as my_file:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_file}
        result = [profit, {'Средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                           len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, new_file, ensure_ascii=False)