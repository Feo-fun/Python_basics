with open('text_2.txt', 'r', encoding='utf-8') as my_file:
    el_count = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов'
                for line, count in enumerate(my_file, 1)]
    print(*el_count, f'Всего строк - {len(el_count)}.', sep='\n')