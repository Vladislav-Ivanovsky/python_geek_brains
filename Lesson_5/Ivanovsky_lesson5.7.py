# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

firms_statistic = {}
avg_profit = {}
with open(r"resources\firms_data.txt", encoding="utf8") as file_read_obj:
    for firm in file_read_obj:
        firm_name, firm_data = firm.split(":")
        firm_figures = [*map(int, str(firm_data).strip().split(" ")[1:3])]
        firms_statistic[firm_name] = firm_figures[0] - firm_figures[1]
profits = [*filter(lambda x: x >= 0, firms_statistic.values())]
avg_profit["Average_profit"] = sum(profits) / len(profits)
with open(r"firms_data_json.txt", "w", encoding="utf8") as file_write_obj:
    json.dump([firms_statistic, avg_profit], file_write_obj, ensure_ascii=False)
