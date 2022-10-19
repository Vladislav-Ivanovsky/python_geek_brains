# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(dividend, divisor):
    """ Возвращает частное от деления

    :param dividend: делимое
    :param divisor: делитель

    """
    if divisor == 0:
        return "Ошибка деления на ноль"
    return dividend / divisor


user_input = input("Введите делимое и делитель через '/' (например 4.5/2.5): ")
dividend, divisor = list(map(float, user_input.split('/')))

print(f"{dividend} / {divisor} = {div(dividend, divisor)}")
