class Worker:

    """Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def get_full_name(self):
        return self.name.title() + ' ' + self.surname.title()


my_income = {'wage': 100, 'bonus': 50}
my_worker = Position('ee', 'gg', 'chef', my_income)
print(my_worker.get_total_income())
print(my_worker.get_full_name())

