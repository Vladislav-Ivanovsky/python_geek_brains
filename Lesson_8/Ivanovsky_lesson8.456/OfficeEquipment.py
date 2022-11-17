# модуль описывает классы отвечающие за конкретный тип оргтехники
# каждый класс умеет:
# 1. запросить у пользователя ввод атрибутов, за которые класс отвечает
# 2. для объекта - вывести значения всех атрибутов, за которые он отвечает
# 3. вернуть строку описывающую тип оргтехники, за которую он отвечает
# 4. для объекта - вернуть строку с названием модели

from abc import ABC, abstractmethod


# зададим, какие методы должен определить каждый класс описывающий оргтехнику
# кстати, фокус с обязательным определением абстрактных методов не сработает при двухступенчатом наследовании
# например если для MFP не перегрузить get_equipment_type_name(), то интерпретатор ругаться не будет
# т.к. этот метод определён в Printer
class AbstractEquipment(ABC):
    # перегрузка __hash__ и __eq__ требуется,
    # чтобы объект использовался как ключ с dict
    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    # перегрузка __str__ нужна для отображения объекта
    @abstractmethod
    def __str__(self):
        pass

    # нужен, чтобы объект каждого класса мог сообщить характеристики модели оргтехники, которую он описывает
    @abstractmethod
    def say_about_yourself(self):
        pass

    # используется, чтобы класс сообщал за какой тип оргтехники он отвечает
    @staticmethod
    @abstractmethod
    def get_equipment_type_name():
        pass


class OfficeEquipment(AbstractEquipment):
    # каждый класс будет содержать перечень своих атрибутов, перечисленных в словаре equipment_attributes
    # состав элемента словаря:
    # ключ - код атрибута
    # значение - список, содержащий:
    #   1. Название атрибута для вывода на экран
    #   2. строка валидации. Поддерживает следующие значения:
    #       - None - валидация отсутствует. Любая последовательность символов
    #       - int - значение параметра должно задаваться целым числом
    #       - список строк разделенных символом слэш '/' - допустимо только одно из указанных значений
    #   3. Обязательность заполнения. "R" - атрибут обязателен к заполнению. "O" - атрибут не обязателен для заполнения
    equipment_attributes = {"name": ["Название модели", None, "R"],
                            "vendor": ["Производитель (например Epson)", None, "R"],
                            "max_paper_size": ["Максимальный размер бумаги (например A4)", None, "O"],
                            "is_network": ["Доступ по сети (Y/N)", "Y/N", "O"],
                            "is_wireless": ["Беспроводной доступ (Y/N)", "Y/N", "O"]}

    def __init__(self, args):
        # я решил не заводить явно атрибуты для каждого класса, т.к. они не используются в программе
        # вместо этого я воспользуюсь словарём и буду хранить данные там
        # но, каждый класс будет содержать свой словарь с перечнем кодов атрибутов, специфичных именно для него
        self._equipment = args

    # методы __hash__ и __eq__ достаточно определить только в OfficeEquipment
    # далее их наследуют потомки и это позволяет им выступать ключами словаря тоже
    def __hash__(self):
        return hash(self._equipment["vendor"] + self._equipment["name"])

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return self._equipment["vendor"] + " " + self._equipment["name"]

    def say_about_yourself(self):
        """ Запрашивает вывод на экран общих параметров оргтехники.
            Потомки должны перегружать этот метод так,
            чтобы сперва вызывался родительский метод say_about_yourself
            (удобнее, когда сперва пользователь видит общую информацию о модели,
             как минимум название и производителя)
        """
        self._print_object_data(OfficeEquipment.equipment_attributes)

    def _print_object_data(self, attributes_to_print):
        """ выводит на экран параметры оргтехники, заданные в attributes_to_print

        :param attributes_to_print: какие параметры оргтехники вывести на экран
        """
        for attr_code, attr_list in attributes_to_print.items():
            # не будем выводить те параметры, значения для которых не заданы
            if self._equipment.get(attr_code) is not None:
                print(f"{attr_list[0]}: {self._equipment[attr_code]}")

    @classmethod
    def initialize(cls):
        """ Запрашивает ввод данных, необходимых для инициализации конкретного класса
            При этом список атрибутов для заполнения определяется тем какой класс создаём по иерархии наследования
        """
        class_set = {cls}
        # получим список всех базовых классов данного класса
        for base_class in cls.__bases__:
            if base_class is not OfficeEquipment:
                class_set.add(base_class)

        # переупорядочим список так, чтобы OfficeEquipment шёл первым
        class_list = [OfficeEquipment, *class_set]
        equipment_dictionary = {}

        # а теперь для каждого класса запросим его специфические атрибуты
        for class_item in class_list:
            for key, value in class_item.equipment_attributes.items():
                while True:
                    user_input = input(f"{value[0]}: ")
                    # Проверим введённые данные
                    if value[1] is None:
                        break
                    if len(user_input) == 0:
                        if value[2] == "R":
                            print(f"Атрибут {value[0]} обязателен к заполнению")
                            continue
                        else:
                            break
                    if value[1] == "int":
                        if not user_input.isdecimal():
                            print("Необходимо ввести число!")
                            continue
                        else:
                            break
                    list_for_check = value[1].split("/")
                    check_passed = False
                    for element in list_for_check:
                        if element.upper() == user_input.upper():
                            check_passed = True
                            break
                    if not check_passed:
                        print(f"Атрибут {value[0]} допускает только значения {value[1]}!")
                        continue
                    break
                equipment_dictionary[key] = user_input

        # на базе собранных данных создадим объект класса и вернём его
        return cls(equipment_dictionary)

    @staticmethod
    def get_all_equipment_classes(parent_cls=None):
        """ Собирает и возвращает все классы потомки OfficeEquipment в виде словаря, где:
            ключ - тип оргтехники; значение - класс, который за него отвечает
            (У каждого класса потомка есть статический метод get_equipment_type_name(),
            который возвращает тип оборудования за который отвечает класс)
        """
        all_equipments = {}
        parent_cls = OfficeEquipment if parent_cls is None else parent_cls
        for cls in parent_cls.__subclasses__():
            all_equipments.update({cls.get_equipment_type_name(): cls})
            for equipment_name, equipment_class in OfficeEquipment.get_all_equipment_classes(cls).items():
                all_equipments.update({equipment_name: equipment_class})
        return all_equipments


class Printer(OfficeEquipment):
    # перечень атрибутов, специфичных для принтеров
    equipment_attributes = {"is_colour": ["Цветной (Y/N)", "Y/N", "R"],
                            "is_duplex": ["Двусторонняя печать (Y/N)", "Y/N", "R"],
                            "bw_print_pages_per_minute": ["Скорость ч/б печати (стр/мин)", "int", "O"],
                            "colour_print_pages_per_minute": ["Скорость цветной печати (стр/мин)", "int", "O"],
                            "printer_type": ["Тип принтера (лазерный/струйный/матричный)",
                                             "лазерный/струйный/матричный", "R"],
                            "max_print_dpi": ["Максимальное разрешение печати dpi (например 1200x1200)", None, "R"]}

    def __init__(self, args):
        super().__init__(args)

    def __str__(self):
        return "Принтер " + OfficeEquipment.__str__(self)

    def say_about_yourself(self):
        super().say_about_yourself()
        self._print_object_data(Printer.equipment_attributes)

    @staticmethod
    def get_equipment_type_name():
        return "Принтер"


class Scaner(OfficeEquipment):
    # перечень атрибутов, специфичных для сканеров
    equipment_attributes = {"scaner_type": ["Датчик (CIS/CCD)", "CIS/CCD","R"],
                            "max_scan_dpi": ["Максимальное разрешение сканирования dpi (например 1200x1200)", None, "R"],
                            "max_scan_pages_per_minute": ["Максимальная скорость сканирования (стр/мин)", "int", "O"]}

    def __init__(self, args):
        super().__init__(args)

    def __str__(self):
        return "Сканер " + OfficeEquipment.__str__(self)

    def say_about_yourself(self):
        super().say_about_yourself()
        self._print_object_data(Scaner.equipment_attributes)

    @staticmethod
    def get_equipment_type_name():
        return "Сканер"


# я не смог удержаться и не поиграть с множественным наследованием :)
class MFP(Printer, Scaner):
    # перечень атрибутов, специфичных для МФУ
    # даже если атрибутов нет, атрибут equipment_attributes всё равно должен быть задан
    equipment_attributes = {}

    def __init__(self, args):
        # тут будет интересно. Так как конструктор каждого класса-потомка вызывает конструктор родителя,
        # то очерёдность вызовов для MFP будет такой:
        # MFP.__init__
        # Printer.__init__
        # Scaner.__init__
        # OfficeEquipment.__init__ <-- тут и произойдет создание и инициализация self._equipment
        super().__init__(args)

    def __str__(self):
        return "МФУ " + OfficeEquipment.__str__(self)

    def say_about_yourself(self):
        # Так как каждый класс-потомок сперва вызывает метод say_about_yourself родителя
        # и только потом выводит на экран информацию о себе, то для MFP получится так:
        # OfficeEquipment выводит значение своих атрибутов на экран
        # Scaner выводит значение своих атрибутов на экран
        # Printer выводит значение своих атрибутов на экран
        # MFP выводит значение своих атрибутов на экран (правда выводить нечего:)
        super().say_about_yourself()
        self._print_object_data(MFP.equipment_attributes)

    @staticmethod
    def get_equipment_type_name():
        return "МФУ"

# Если мы добавим нового потомка, описывающего новый тип оргтехники, и он правильно описан, то в остальных классах
# ничего менять не потребуется - новый класс подхватится автоматически.
#
# Класс-потомок описан правильно если:
# 1. у него задан атрибут класса - словарь equipment_attributes, где каждый элемент отвечает за специфичный для этого
#   типа оргтехники атрибут (см. подробное описание в комментарии к классу OfficeEquipment)
# 2. его конструктор вызывает конструктор базового класса и передаёт туда переменную (в нашем случае - args)
# 3. у него перегружен метод __str__
# 4. у него перегружен метод say_about_yourself следующим образом:
#        super().say_about_yourself()
#        self._print_object_data(<name of new child>.equipment_attributes)
# 5. у него описан статический метод get_equipment_type_name, возвращающий название типа оргтехники
