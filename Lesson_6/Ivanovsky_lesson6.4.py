# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.__car_prefix = "Полицейский автомобиль" if self.is_police else "Автомобиль"
        self._full_car_name = f"{self.__car_prefix} {self.color} '{self.name}'"

    def go(self, speed):
        print(f"{self._full_car_name} начал движение")
        self.speed = speed

    def stop(self):
        print(f"{self._full_car_name} остановился")
        self.speed = 0

    def turn(self, direction):
        print(f"{self._full_car_name} повернул {direction}")

    def show_speed(self):
        if self.speed == 0:
            print(f"{self._full_car_name} стоит на месте")
        else:
            print(f"{self._full_car_name} двигается со скоростью {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed < 60:
            super().show_speed()
        else:
            print(f"{self._full_car_name} нарушает скоростной режим (скорость = {self.speed} км/ч)")


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed < 40:
            super().show_speed()
        else:
            print(f"{self._full_car_name} нарушает скоростной режим (скорость = {self.speed} км/ч)")


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self._full_car_name = f"Спортивный автомобиль {self.color} '{self.name}'"


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, is_police=True)


town_car = TownCar("белый", "VolksWagen Touareg")
work_car = WorkCar("чёрный", "ВАЗ 2121 Нива")
sport_car = SportCar("серебристый", "Lamborghini Morcielago")
police_car = PoliceCar("чёрный", "Land Cruiser 200")

cars = [town_car, work_car, sport_car, police_car]
for car in cars:
    print(f"Атрибуты объекта класса {type(car)}: {car.__dict__}")
    car.show_speed()
    car.go(30)
    car.turn("направо")
    car.show_speed()
    car.speed = 50
    car.show_speed()
    car.turn("налево")
    car.speed = 120
    car.show_speed()
    car.stop()
    car.show_speed()
    print("")
