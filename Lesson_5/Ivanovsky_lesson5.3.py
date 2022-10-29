# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

import functools

print("Сотрудники с доходом менее 20 000:")
salaries = []
with open(r"resources\Employees.txt", encoding="utf8") as file_obj:
    for file_string in file_obj:
        surname, salary = file_string.split(" ")
        if int(salary) < 20000:
            print(f"{surname}:{int(salary)}")  # делаю здесь преобразование к int, чтобы удалить \n на конце salary
        salaries.append(int(salary))
avg_salary = functools.reduce(lambda x, y: x + y, salaries) / len(salaries)
print(f"\nСредняя зарплата (через reduce+lambda) = {avg_salary:.2f}")
print(f"Средняя зарплата (через sum) = {sum(salaries) / len(salaries):.2f}")
