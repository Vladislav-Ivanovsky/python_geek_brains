# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

user_input = input("Введите набор натуральных чисел (через запятую): ")
natural_numbers_list = list(map(int, user_input.split(',')))
natural_numbers_list.sort(reverse=True)
print(f"Отсортированный по убыванию набор: {natural_numbers_list}")
one_more_natural_number = int(input("Введите натуральное число для добавления в набор: "))
natural_numbers_list.append(one_more_natural_number)
natural_numbers_list.sort(reverse=True)
print(f"Отсортированный по убыванию набор c новым числом: {natural_numbers_list}")
