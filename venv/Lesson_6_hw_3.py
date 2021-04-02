class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'Имя - {self.name}, фамилия - {self.surname}'

    def get_total_income(self):
        return f'Суммарный доход - {sum(self._income.values())}'

manager = Position('Klava', 'Pupkina', 'product manager', 15000, 10000)

print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())
