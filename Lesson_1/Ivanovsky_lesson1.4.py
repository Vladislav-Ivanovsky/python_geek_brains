# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
inputed_number = input("Введите целое положительное число: ")
max_number = 0
digit_number = len(inputed_number) - 1
number = int(inputed_number)
while digit_number > 0:
    digit_value = number // (10 ** digit_number)
    if digit_value > max_number:
        max_number = digit_value
    number = number - digit_value * (10 ** digit_number)
    digit_number = digit_number - 1
print(f"Самая большая цифра в числе {inputed_number} = {max_number}")
