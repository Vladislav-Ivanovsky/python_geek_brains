# Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.

class Road:
    def __init__(self, length, width, weight_1m_1cm=25.0, thickness_in_cm=5):
        self.__length = length
        self.__width = width
        self.__weight_1m_1cm = weight_1m_1cm
        self.thickness_in_cm = thickness_in_cm

    def get_total_weight(self):
        return self.__length * self.__width * self.__weight_1m_1cm * self.thickness_in_cm


road1 = Road(length=10000, width=6)
road2 = Road(length=30000, width=6, weight_1m_1cm=25.7)
road3 = Road(length=50000, width=6, weight_1m_1cm=24.2, thickness_in_cm=6)

print(f"Масса асфальта для первой дороги: {road1.get_total_weight()} кг")
print(f"Масса асфальта для второй дороги: {road2.get_total_weight()} кг")
print(f"Масса асфальта для третьей дороги: {road3.get_total_weight()} кг")
