# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, actual, imaginary):
        self.__actual = actual
        self.__imaginary = imaginary

    def __str__(self):
        img_str = '+' if self.__imaginary > 0 else ''
        img_str = img_str + ('-' if self.__imaginary < 0 else '')
        img_str = img_str + (str(abs(self.__imaginary)) if abs(self.__imaginary) > 1 else '')
        img_str = img_str + ('i' if self.__imaginary != 0 else '')
        return f"{self.__actual}{img_str}"

    @property
    def actual(self):
        return self.__actual

    @property
    def imaginary(self):
        return self.__imaginary

    def __add__(self, other):
        return ComplexNumber(self.actual + other.actual, self.imaginary + other.imaginary)

    def __mul__(self, other):
        act = self.actual * other.actual - self.imaginary * other.imaginary
        img = self.imaginary * other.actual + self.actual * other.imaginary
        return ComplexNumber(act, img)


cn1 = ComplexNumber(2, 1)
cn2 = ComplexNumber(3, 4)
print(f"Результат сложения с помощью класса ComplexNumber: ({cn1}) + ({cn2}) = {cn1 + cn2}")
print(
    f"Результат сложения с помощью встроенного типа complex: ({cn1}) + ({cn2}) ="
    f" {complex(cn1.actual, cn1.imaginary) + complex(cn2.actual, cn2.imaginary)}")

cn1 = ComplexNumber(2, 5)
cn2 = ComplexNumber(1, -7)
print(f"\nРезультат сложения с помощью класса ComplexNumber: ({cn1}) + ({cn2}) = {cn1 + cn2}")
print(
    f"Результат сложения с помощью встроенного типа complex: ({cn1}) + ({cn2}) ="
    f" {complex(cn1.actual, cn1.imaginary) + complex(cn2.actual, cn2.imaginary)}")

cn1 = ComplexNumber(1, 2)
cn2 = ComplexNumber(3, -1)
print(f"\nРезультат умножения с помощью класса ComplexNumber: ({cn1}) x ({cn2}) = {cn1 * cn2}")
print(
    f"Результат умножения с помощью встроенного типа complex: ({cn1}) x ({cn2}) ="
    f" {complex(cn1.actual, cn1.imaginary) * complex(cn2.actual, cn2.imaginary)}")
