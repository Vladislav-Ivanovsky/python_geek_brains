# Поработайте с переменными, создайте несколько, выведите на экран.

str_sample = "Работаем с переменными"
decimal_sample = 10
float_sample = 30.589424
boolean_sample = False
list_sample = list('list')
tuple_sample = tuple('tuple')
dict_sample = {3: "list", 2: "tuple", 1: "dict"}

print(str_sample)
print("Decimal sample: ", decimal_sample)
print("Float sample: %.3f" % float_sample)
print("Boolean sample: {}".format(boolean_sample))
print(f"List_sample: {list_sample}")
list_sample[0] = 'z'
print(f"List_sample after change: {list_sample}")
print(f"Let's get the first element of List_sample: {list_sample[0]}")
print(f"Tuple_sample: {tuple_sample}")
# Раскомментируйте строку ниже и интерпретатор выдаст ошибку, что tuple не поддерживает изменение объекта
# tuple_sample[0]='z'
print(f"Dict_sample: {dict_sample}")
print(f"Let's get Dict_sample element by key='1': {dict_sample[1]}")

# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
result = input("\nВам понравилось как я выполнил задание? (Y/N): ")
if result == "Y":
    print("Я рад :)")
elif result == "N":
    print("Эх, жаль :(")
else:
    print("Округлю в свою пользу ;)")

score = int(input("\nОцените мой результат по 5-ти бальной шкале (как в школе): "))
if score < 1:
    print("Вы слишком строги ко мне :)")
elif score in [1, 2]:
    print("Так плохо я никогда не учился :(")
elif score in [3, 4]:
    print("Есть куда расти :)")
else:
    print("Спасибо!")
