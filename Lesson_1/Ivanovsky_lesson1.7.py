# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_day_distance = int(input("Введите, какую дистанцию (в км) пробежал спортсмен в 1й день: "))
final_distance = int(input("Введите, какую дистанцию (в км) он должен пробежать: "))
day_num = 1
last_result = first_day_distance
while last_result < final_distance:
    day_num = day_num + 1
    last_result = 1.1 * last_result
    if day_num > 36500:
        break

# сформируем правильно строку
last_digit = day_num % 10
before_last_digit = (day_num % 100) // 10
day_word_form = 'дней'
if last_digit == 1 and before_last_digit != 1:
    day_word_form = 'день'
elif last_digit in [2, 3, 4] and before_last_digit != 1:
    day_word_form = 'дня'

if day_num > 36500:
    print("Спортсмену не хватит жизни, чтобы натренироваться пробегать нужную дистанцию")
else:
    print(f"Спортсмену потребуется {day_num} {day_word_form}, чтобы натренироваться пробегать дистанцию в {final_distance} км")
