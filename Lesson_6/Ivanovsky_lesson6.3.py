# Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos1 = Position("Владислав", "Ивановский", "массовик-затейник", wage=100000, bonus=50000)
pos2 = Position("Михаил", "Мишустин", "премьер-министр", wage=400000, bonus=1000000)
pos3 = Position("Фрэнк", "Абигнейл", "аферист", wage=600000, bonus=20000000)

positions = [pos1, pos2, pos3]

for pos in positions:
    print(f"Атрибуты объекта:\n{pos.__dict__}\n")
    print(f"Данные по позиции '{pos.position}'")
    print(f"Работник: {pos.get_full_name()}")
    print(f"Доход: {pos.get_total_income()}")
    print(f"Раскрытие дохода - Оклад: {pos._income['wage']}, Премия: {pos._income['bonus']}\n")
