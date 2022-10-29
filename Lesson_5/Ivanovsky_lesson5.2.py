# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

def is_word(sequence):
    """ Проверяет, что переданная последовательность - это слово

    :param sequence: переданная последовательность
    """
    # почистим последовательность от знаков препинания
    for char_to_remove in ".,-:'\";\n()“”/\\":
        sequence = sequence.replace(char_to_remove, '')
    # и, собственно проверим - слово ли это
    return sequence.isalpha()


# пример работы с контекстом файла
string_amount = 0
words_amount = 0
with open(r"resources\Eula.txt") as file_obj:
    for string in file_obj:
        string_amount += 1
        words_amount += len([el for el in string.split(" ") if is_word(el)])

print(f"Количество строк в файле = {string_amount}")
print(f"Количество слов в файле = {words_amount}")
