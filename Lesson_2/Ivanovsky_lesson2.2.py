# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

user_input = input("Введите список (значения разделяются запятой): ")
my_list = list(user_input.split(','))
print(my_list)
for i in range(len(my_list) // 2):
    my_list[i * 2], my_list[i * 2 + 1] = my_list[i * 2 + 1], my_list[i * 2]
print(f"{my_list}")
