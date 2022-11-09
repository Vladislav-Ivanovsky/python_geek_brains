# Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

# хочется сделать красиво - а почему бы не нарисовать светофор и заставить его работать ))
# а раз так - почему бы не создать несколько светофоров и пусть работают одновременно
# для этого я перелопатил pyplot и нашёл как сделать анимированный светофор
# но это потребовало особого подхода к методу run - он должен быть статическим
# и вызываться после создания объектов всех светофоров

import matplotlib.pyplot as plt
import matplotlib.animation as anim


class TrafficLight:
    def __init__(self, red_delay, yellow_delay, green_delay, state_machine=None):
        """ конструктор светофора, он задаст начальное состояние светофора и подготовит его к отображению

        :param red_delay: задержка для красного сигнала
        :param yellow_delay: задержка для жёлтого сигнала
        :param green_delay: задержка для зелёного сигнала
        """

        # Чтобы реализовать усложнённый вариант задания позволим задавать любую последовательность переключения
        # Если не задана - используем последовательность по умолчанию и считаем, что светофор работает в обычном режиме
        # Если задана и она валидна - то будем считать, что светофор работает в ручном режиме

        normal_state_machine = ("red", "yellow", "green", "yellow")
        mode = "Обычный режим"

        if state_machine is None:
            self.__state_machine = normal_state_machine
        elif type(state_machine) is not tuple:  # придётся проверить, что нам всё передали верно
            print("Сбой инициализации светофора - последовательность состояний должна передаваться через tuple")
            return
        elif len(state_machine) == 0:
            print("Сбой инициализации светофора - надо задать хотя бы одно состояние")
            return
        else:
            for state in state_machine:
                if state not in ["red", "yellow", "green"]:
                    print("Сбой инициализации светофора - допустимы только состояния 'red', 'yellow', 'green'")
                    return
            self.__state_machine = state_machine

        if self.__state_machine != normal_state_machine:
            mode = "Ручной режим"

        # Инициализируем генератор для перебора состояний светофора
        self.__state_machine_gen = self.__state_machine_generator()

        # Каждое состояние светофора описывается следующим образом:
        # "название состояния":(задержка,(RGB красного, RGB жёлтого, RGB зелёного))
        self.__traffic_light_states = {"red": (red_delay, ("#a52019", "#bbbbbb", "#bbbbbb")),
                                       "yellow": (yellow_delay, ("#bbbbbb", "#e5be01", "#bbbbbb")),
                                       "green": (green_delay, ("#bbbbbb", "#bbbbbb", "#317f43"))}
        # зададим словарь RGB цветов для кол-ва секунд
        self.__counter_colors = {"red": "#a52019", "yellow": "#e5be01", "green": "#317f43"}

        # инициализируем список графических объектов, отвечающих за красный, жёлтый и зелёный цвета светофора
        self.__lights = []
        for y in range(15, 4, -5):
            self.__lights.append(plt.Circle((10, y), radius=2))

        # как вы просили - назовём состояние светофора color и он - приватный
        self.__color = next(self.__state_machine_gen)

        # вся анимация светофора построена вокруг matplotlib.animation.FuncAnimation
        # Она раз в секунду будет вызывать метод обновления состояния светофора
        # Приватный атрибут __ticks будет считать сколько прошло секунд, чтобы определять - надо ли выполнять
        # переключение состояния
        self.__ticks = 0

        # подготавливаем pyplot для отрисовки светофора
        self.__fig = plt.figure(figsize=(200 / 100, 480 / 100), dpi=100)

        # сдвигаем окно, чтобы светофоры не перекрывали друг друга
        plt.gcf().canvas.manager.window.move(220 * (plt.gcf().number - 1), 0)
        # укажем название окна
        plt.gcf().canvas.manager.set_window_title(f"Светофор {plt.gcf().number}")

        # эта переменная будет хранить ссылку на объект, отображающий над светофором кол-во секунд
        self.__counter_text = plt.gca().text(10, 18, '')
        self.__counter_text.set_fontweight('semibold')

        # укажем в каком режиме работает светофор
        if mode == "Обычный режим":
            plt.gca().text(6, 20, mode, color="#317f43").set_fontweight('semibold')
        else:
            plt.gca().text(7, 20, mode, color="#a52019").set_fontweight('semibold')

        # проинициализируем светофор - зададим начальное состояние сигналов и укажем кол-во секунд
        self.__set_traffic_state()

        # добавим круги светофора в axes
        for light in self.__lights:
            plt.gca().add_artist(light)

        # установим одинаковый масштаб для осей x и y
        plt.axis("equal")
        # отключим отображение осей и их подписи
        plt.axis("off")
        # укажем предельные значения осей x и y
        plt.axis([0, 20, 0, 20])

        # указываем какая функция будет анимировать светофор раз в секунду
        self.__animation = anim.FuncAnimation(self.__fig, self.__tick, interval=1000)

    def __state_machine_generator(self):
        for color in self.__state_machine:
            yield color

    def __set_traffic_state(self):
        """ переводит светофор в состояние указанное в self.__color
        """
        delay, lights_colors = self.__traffic_light_states[self.__color]
        for pair in zip(self.__lights, lights_colors):
            pair[0].set_color(pair[1])
        self.__counter_text.set_color(self.__counter_colors[self.__color])
        self.__counter_text.set_text(str(delay))

    def __tick(self, frame):
        """ запускается каждую секунду, обновляет счётчик кол-ва секунд
            и запускает обновление светофора когда время истекло

        :param frame: порядковый номер запуска метода
        """

        delay, lights_colors = self.__traffic_light_states[self.__color]
        # если время не истекло - просто обновляем счётчик секунд
        if self.__ticks < delay:
            self.__ticks += 1
            self.__counter_text.set_text(str(delay - self.__ticks))
            return

        # иначе переходим в следующее состояние и обновляем светофор
        self.__color = next(self.__state_machine_gen, None)
        if self.__color is None:
            self.__state_machine_gen = self.__state_machine_generator()
            self.__color = next(self.__state_machine_gen, None)

        self.__set_traffic_state()
        self.__ticks = 0

    @staticmethod
    def run():
        """ статический метод запуска всех светофоров
            на настоящий момент я смог реализовать только такой подход с прорисовкой

        """
        plt.show()


# пытаемся создать объекты светофоров
# для случаев, когда передаётся неверный machine_state будет выдано сообщение об ошибке
# и светофоры отображаться не будут
t1 = TrafficLight(red_delay=7, yellow_delay=2, green_delay=10)  # вариант из задания
t2 = TrafficLight(red_delay=8, yellow_delay=1, green_delay=20, state_machine=("red", "yellow", "green", "yellow"))
t3 = TrafficLight(red_delay=2, yellow_delay=1, green_delay=4,
                  state_machine=("red", "green", "yellow", "green", "red", "yellow"))
t4 = TrafficLight(red_delay=3, yellow_delay=1, green_delay=3, state_machine=())
t5 = TrafficLight(red_delay=1, yellow_delay=1, green_delay=1, state_machine=["red", "yellow", "green"])
t6 = TrafficLight(red_delay=1, yellow_delay=1, green_delay=1, state_machine=("red", "yellow", "green", "orange"))

# и запускаем светофоры
# для завершения работы программы закройте окна со всеми светофорами
TrafficLight.run()
