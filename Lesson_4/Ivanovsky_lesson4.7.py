# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
# следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
# нужно выводить только первые n чисел, начиная с 1! и до n!.

def fact(n):
    result = 1
    for el in range(1, n + 1):
        result *= el
        yield result


max_factorial_base = int(input("Введите максимальное число ряда, для которого будем считать факториал: "))
factorial_generator = fact(max_factorial_base)
print([el for el in factorial_generator])
