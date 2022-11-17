# класс реализует иерархию меню для управления складом
# я постарался сделать его как можно более независимым -
# по большому счёту он может вообще нигде явно не обращаться к классам потомкам OfficeEquipment

from WareHouse import *
from OfficeEquipment import *


class BusinessProcess:
    def __init__(self):
        # зададим набор операций, доступных пользователю
        self.__operations = ["Добавить позицию", "Принять товар", "Отпустить товар", "Информация о товаре", "Выход"]

        # получим список типов техники, которые реализованы всеми потомками OfficeEquipment
        # каждый элемент словаря представлен парой {Название типа оргтехники: Класс}
        # такой словарь позволяет вызывать методы нужного класса не обращаясь в нему напрямую
        self.__equipments = dict(OfficeEquipment.get_all_equipment_classes())

        # создадим склад и проинициализируем его некоторыми начальными позициями
        self.__warehouse = WareHouse()
        mfp_1 = {"name": "LaserJet Pro MFP M428dw", "vendor": "HP", "max_print_dpi": "3600x3600",
                 "max_paper_size": "A4",
                 "is_network": 'Y', "is_wireless": 'Y', "is_colour": 'N', "printer_type": "лазерный",
                 "is_duplex": 'Y',
                 "bw_print_pages_per_minute": 38, "scaner_type": "CIS", "max_scan_dpi": "1200x1200",
                 "max_scan_pages_per_minute": 12}

        mfp_2 = {"name": "L8180", "vendor": "Epson", "max_print_dpi": "576x1440", "max_paper_size": "A4",
                 "is_network": 'Y', "is_wireless": 'Y', "is_colour": 'Y', "printer_type": "струйный",
                 "is_duplex": 'Y',
                 "bw_print_pages_per_minute": 16, "colour_print_pages_per_minute": 17, "scaner_type": "CIS",
                 "max_scan_dpi": "1200x4800"}

        printer_1 = {"name": "L805", "vendor": "Epson", "max_print_dpi": "5760x1440", "max_paper_size": "A4",
                     "is_network": 'Y', "is_wireless": 'Y', "is_colour": 'Y', "printer_type": "струйный",
                     "is_duplex": 'N',
                     "bw_print_pages_per_minute": 37, "colour_print_pages_per_minute": 38}

        printer_2 = {"name": "Phaser 3020", "vendor": "Xerox", "max_print_dpi": "1200x1200", "max_paper_size": "A4",
                     "is_network": 'Y', "is_wireless": 'Y', "is_colour": 'Y', "printer_type": "лазерный",
                     "is_duplex": 'Y',
                     "bw_print_pages_per_minute": 20}

        scaner_1 = {"name": "Canonscan LIDE300", "vendor": "Canon", "max_paper_size": "A4", "is_network": 'N',
                    "is_wireless": 'N', "scaner_type": "CIS", "max_scan_dpi": "2400x2400"}

        scaner_2 = {"name": "ADS-2700W", "vendor": "Brother", "max_paper_size": "A4", "is_network": 'Y',
                    "is_wireless": 'Y', "scaner_type": "CIS", "max_scan_dpi": "1200x1200",
                    "max_scan_pages_per_minute": 35}

        # тут я отошёл от правила не обращаться к названиям классов оргтехники напрямую, чтобы заполнить чем-то склад
        # в принципе можно убрать эти три строчки, и всё будет работать, только склад придётся заполнять вручную
        list_of_devices = [MFP(mfp_1), MFP(mfp_2), Printer(printer_1), Printer(printer_2), Scaner(scaner_1),
                           Scaner(scaner_2)]

        for device in list_of_devices:
            self.__warehouse.add_position(device)

    def run(self):
        print("\nДобро пожаловать в программу складского учёта 'Vlad & Son Co'Ⓡ")
        while True:
            print("\nВыберите операцию:")
            point = self.__select_point(self.__operations)
            if point == "Добавить позицию":
                self.__add_position()
            elif point == "Принять товар":
                self.__receipt()
            elif point == "Отпустить товар":
                self.__release()
            elif point == "Информация о товаре":
                print("\nВыберите интересующий товар:")
                user_select = self.__select_point(self.__warehouse.get_positions(), "<-- Предыдущий пункт меню")
                if user_select != "<-- Предыдущий пункт меню":
                    print(f"\nИнформация о товаре '{user_select}'")
                    # user_select содержит объект, описывающий конкретную модель оргтехники
                    # попросим его вывести информацию о себе
                    user_select.say_about_yourself()
            elif point == "Выход":
                print("Работа завершена. Хорошего дня!")
                break

    def __select_point(self, data, *firstpoints):
        """
        Метод делает следующее:
        1. Формирует на экране нумерованный список из элементов списка firstpoints
            и элементов списка data или ключей словаря data (смотря, что передали в метод)
        2. Предлагает пользователю выбрать один из отображенных элементов и проверяет корректность ввода

        :param data: список или словарь, из которого формируется список
                     (например типы оргтехники, товары на складе, доступные операции)
        :param firstpoints: список, содержащий дополнительные элементы, вставляемые в начало списка на экране.
                            Он нужен, чтобы добавить доп. элементы типа "<-- вернуться в меню" и т.д.
        :return: Возвращает выбранный элемент списка или ключ словаря (а не номер под которым выводился элемент/ключ)
        """
        if type(data) is list:
            point_names = data
        elif type(data) is dict:
            point_names = list(dict(data).keys())
        for number, element_name in enumerate(firstpoints, start=1):
            print(f"{number}. {element_name}")
        for number, element_name in enumerate(point_names, start=len(firstpoints) + 1):
            print(f"{number}. {element_name}")
        point_amounts = len(firstpoints) + len(point_names)
        user_input = '0'
        while True:
            user_input = input("Введите номер пункта и нажмите Enter: ")
            if not user_input.isdecimal():
                print("Необходимо ввести число!")
            elif (int(user_input) == 0) or (int(user_input) > point_amounts):
                print("Введите только число из списка!")
            else:
                break
        point = int(user_input)
        if point > len(firstpoints):
            return point_names[point - len(firstpoints) - 1]
        else:
            return firstpoints[point - 1]

    def __add_position(self):
        print("Выберите тип техники, который хотите добавить:")
        user_select = self.__select_point(self.__equipments, "<-- Предыдущий пункт меню")
        if user_select == "<-- Предыдущий пункт меню":
            return None
        # user_select содержит название типа техники
        # теперь с его помощью выбираем из словаря нужный подкласс OfficeEquipment и запускаем инициализацию
        equipment = self.__equipments[user_select].initialize()

        # ну и добавляем созданный объект на склад.
        # теперь склад знает про такой товар и можно выполнять приёмку
        self.__warehouse.add_position(equipment)
        return equipment

    def __receipt(self):
        while True:
            print("\nВыберите принимаемый товар:")
            positions = self.__warehouse.get_positions()
            user_select = self.__select_point(positions, "<-- Предыдущий пункт меню", "Добавить позицию")
            if user_select == "Добавить позицию":
                user_select = self.__add_position()
                if user_select is None:
                    continue
            elif user_select == "<-- Предыдущий пункт меню":
                break
            while True:
                user_input = input("Введите количество принимаемого товара: ")
                if not user_input.isdecimal():
                    print("Необходимо ввести число!")
                    continue
                break
            # user_select содержит объект, описывающий конкретную модель оргтехники
            # с помощью этого объекта склад понимает с какой позицией производить манипуляции
            self.__warehouse.receipt(user_select, int(user_input))
            break

    def __release(self):
        while True:
            print("\nВыберите отпускаемый товар:")
            positions = self.__warehouse.get_positions()
            # тут есть смысл добавить к каждой модели оргтехники кол-во на складе, чтобы пользователь не гадал
            # сколько её есть возможность отпустить
            positions = dict(
                map(lambda item: ((str(item[0]) + f" ({item[1]} шт. на складе)"), item[0]), positions.items()))
            user_select = self.__select_point(positions, "<-- Предыдущий пункт меню")
            if user_select == "<-- Предыдущий пункт меню":
                break
            # user_select содержит объект, описывающий конкретную модель оргтехники
            # с помощью этого объекта склад понимает с какой позицией производить манипуляции
            while True:
                amount = input("Введите отпускаемое количество товара: ")
                if not amount.isdecimal():
                    print("Необходимо ввести число!")
                    continue
                break
            destination = input("Введите подразделение куда отпускается товар: ")
            try:
                self.__warehouse.release(positions[user_select], amount=int(amount), destination=destination)
            except WareHouseException as ex:
                print(ex)
                continue
            break
