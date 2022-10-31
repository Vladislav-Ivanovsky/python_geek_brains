# Реализовать скрипт с итератором, генерирующий целые числа, начиная с указанного

from itertools import count

start_number = int(input("Введите начальное число: "))
end_number = int(input("Введите конечное число: "))

for el in count(start_number):
    if el > end_number:
        break
    else:
        print(el)
