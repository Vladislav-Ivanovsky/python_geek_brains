# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def print_user_data(name, surname, year_born, city_live, email, phone):
    """ Печать данных о пользователе

    :param name: имя
    :param surname: фамилия
    :param year_born: год рождения
    :param city_live: город проживания
    :param email: адрес электронной почты
    :param phone: телефон

    """
    print(
        f"Имя:{name}; Фамилия:{surname}; Год рождения:{year_born}; Город проживания:{city_live}; Email:{email}; "
        f"Телефон:{phone}")


print_user_data(surname="Ивановский", name="Владислав", city_live="Санкт-Петербург", email="ivanovsky.v.v@yandex.ru",
                phone="+7 999 888 7766", year_born=1982)
print_user_data(name="Махатма", city_live="Дели", email="free_india@gmail.in", phone="+91 92050 22813", year_born=1869,
                surname="Ганди")
