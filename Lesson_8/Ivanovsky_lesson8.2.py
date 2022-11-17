# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self):
        self.txt = "Деление на ноль запрещено!"

    def __str__(self):
        return self.txt


user_input = ""
while user_input != "stop":
    user_input = input("введите выражение деления в виде x/y (например '15/3'), чтобы выйти введите 'stop': ")
    if user_input == 'stop':
        break
    divividend, divisor = map(int, user_input.split('/'))
    try:
        if divisor == 0:
            raise MyZeroDivisionError
        division = divividend / divisor
        print(f"{divividend}/{divisor} = {division}")
    except MyZeroDivisionError as exception:
        print(exception)
