class WareHouseException(Exception):
    def __init__(self, txt):
        self.txt = txt


# Со складом всё просто.
# На складе есть позиции - это товары, информация о которых известна складу
# Принять на склад можно только тот товар, который складу известен, т.е. по которому существует позиция
# Если необходимо принять товар, по которому нет позиции, то её нужно создать
#
# Самое удобное - склад понятия не имеет, что хранит
# Главное, чтобы объекты, с которыми он работает, могли выступать как ключи словаря склада
# и умели сами себя описывать для формирования сообщений

class WareHouse:
    def __init__(self):
        self.__storage = {}

    def add_position(self, obj):
        self.__storage[obj] = 0
        print(f"Складская позиция '{obj}' добавлена")

    def receipt(self, obj, amount=1):
        """ Приём товара на склад"""
        amount_of_obj = self.__storage.get(obj)
        self.__storage[obj] = amount + (amount_of_obj or 0)
        print(
            f"Товар '{obj}' в количестве {amount} шт. принят на склад. Всего на складе: {self.__storage.get(obj)} шт.")

    def get_positions(self):
        return self.__storage.copy()

    def release(self, obj, destination, amount=1):
        """Отпуск товара со склада"""
        amount_of_obj = self.__storage.get(obj)
        if amount_of_obj is None:
            raise WareHouseException(f"Товара '{obj}' нет на складе")
        elif amount > amount_of_obj:
            raise WareHouseException(
                f"Товара '{obj}' недостаточно на складе. Запрошено: {amount}, На складе:{amount_of_obj}")
        self.__storage[obj] = (amount_of_obj or 0) - amount
        print(
            f"Товар '{obj}' в количестве {amount} шт. отпущен в подразделение '{destination}'. "
            f"Остаток на складе: {self.__storage.get(obj)} шт.")
