# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
import sys

# продемонстрирую заодно понимание stdin, stdout
sys.stdout.write("Вводите строки для записи в файл. Для окончания ввода введите пустую строку.\n")

# работа с файлами без файлового контекста
# я подумал вам будет удобнее читать Unicode текстовые файлы :)
file_obj = open("user_file.txt", "w", encoding="utf8")
while True:
    user_input = sys.stdin.readline()
    if len(user_input) == 1:
        break
    file_obj.write(user_input)
file_obj.close()
