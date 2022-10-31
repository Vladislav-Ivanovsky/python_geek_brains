# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.

import pprint


def clear_string(input_string, strings_to_remove=("(л)", "(лаб)", "(пр)", "\n")):
    """возвращает строку, очищенную от заданных строк
    :param input_string: Строка для очистки
    :param strings_to_remove: строки, которые требуется удалить из очищаемой строки
    """
    for el in strings_to_remove:
        input_string = input_string.replace(el, "")
    return input_string


with open(r"resources\Study plan.txt", encoding="utf8") as file_obj:
    total_hours_dict = {}
    for string in file_obj:
        subject, hours = string.split(":")
        cleared_hours = [int(el) for el in [*map(clear_string, hours.split(" "))] if str(el).isdigit()]
        total_hours_dict[subject] = sum(cleared_hours)
    pprint.pprint(total_hours_dict, sort_dicts=False)
