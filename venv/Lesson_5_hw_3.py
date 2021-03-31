with open('text_3.txt', 'r', encoding='utf-8') as salary:
    employee_salary = {line.split()[0]: float(line.split()[1]) for line in salary}
    print(f'Средняя зарплата сотруднико составляет: {round(sum(employee_salary.values()) / len(employee_salary), 3)}\n'
          f'Сотрудники с зарплатой меньше 20000 рублей: {[el[0] for el in employee_salary.items() if el[1] < 20000]}')

