# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

with open("Numbers_set.txt", "w+") as file_obj:
    rand_list = [random.randint(1, 1000) for el in range(random.randint(1, 100))]
    string_to_file = " ".join([*map(str, rand_list)])
    print(f"Набор чисел: {string_to_file}")
    file_obj.write(string_to_file)
    file_obj.seek(0)
    numbers_from_file = file_obj.readline().split(" ")
    print(f"Сумма чисел: {sum([*map(int, numbers_from_file)])}")
