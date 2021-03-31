russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4_new.txt', 'w', encoding='utf-8') as new_file:
    with open('text_4.txt', 'r', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], russian_dict.get(line.split()[0])) for line in my_file])




