# Реализовать скрипт с итератором, повторяющий элементы некоторого списка, определённого заранее

import random
from itertools import cycle

# чтобы было интересно - сделаем исходный список из случайного набора русских букв
rus_letters = ''.join([chr(el) for el in range(ord('а'), ord('я') + 1)])
rand_string = ''.join([rus_letters[random.randint(0, len(rus_letters) - 1)] for el in range(5)])
print(f"Исходная строка: {rand_string}")
letters_amount = int(input("Введите, сколько букв повторить: "))

final_string = ''
for el in cycle(rand_string):
    final_string += el
    if len(final_string) >= letters_amount:
        break

print(f"Результат повтора: {final_string}")
