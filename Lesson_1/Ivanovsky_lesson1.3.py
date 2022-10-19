# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n_str = input('Введите любую цифру: ')
n = int(n_str)
nn = int(n_str + n_str)
nnn = int(n_str + n_str + n_str)
print(f"{n} + {nn} + {nnn} = {n + nn + nnn}")
