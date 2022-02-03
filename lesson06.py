from itertools import count, cycle
from time import sleep
from datetime import datetime


# 1. Создать класс TrafficLight (светофор).
#
#     определить у него один атрибут color (цвет) и метод running (запуск);
#     атрибут реализовать как приватный;
#     в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#     продолжительность первого состояния (красный) составляет 7 секунд,
#     второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#     переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#     проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    __color = 'red'
    __traffic_timeouts = {'red': 7, 'yellow': 2, 'green': 13}
    __traffic_order = ('red', 'yellow', 'green', 'yellow')
    __color_change_count = 0

    def __init__(self, start_color, **kwargs):
        if kwargs.__contains__('color_change_count') and isinstance(kwargs['color_change_count'], int):
            self.__color_change_count = int(kwargs['color_change_count'])

        if kwargs.__contains__('traffic_timeouts') and isinstance(kwargs['traffic_timeouts'], dict):
            self.__traffic_timeouts = kwargs['traffic_timeouts']
        # if kwargs.__contains__('timeout_red'):
        #     self.__traffic_timeouts['red'] = kwargs['timeout_red']
        # if kwargs.__contains__('timeout_yellow'):
        #     self.__traffic_timeouts['yellow'] = kwargs['timeout_yellow']
        # if kwargs.__contains__('timeout_green'):
        #     self.__traffic_timeouts['green'] = kwargs['timeout_green']

        if kwargs.__contains__('traffic_order') and isinstance(kwargs['traffic_order'], tuple):
            self.__traffic_order = kwargs['traffic_order']

        if self.__traffic_timeouts.__contains__(start_color):
            self.__color = start_color
        else:
            raise Exception(f"Введен неверный цвет {start_color}!")

        print(f"TrafficLight will start with {self.__color} color")

    def running(self):
        generator = (el for el in cycle(self.__traffic_order))
        cur_color = next(generator)
        while cur_color != self.__color:
            cur_color = next(generator)
        cnt = self.__color_change_count
        while True:
            if not self.__traffic_timeouts.__contains__(cur_color):
                raise Exception(f"Последовательность смены режимов нарушена! " +
                                f"По цвету {cur_color} не найдены настройки ожидания (timeout)!")
            cur_color_timeout = self.__traffic_timeouts[cur_color]
            print(f"{cur_color:<7} - {cur_color_timeout:>3}s: {datetime.now():%d.%m.%Y %H:%M:%S}")  # Color
            sleep(cur_color_timeout)  # Timeout
            if self.__color_change_count > 0:
                cnt -= 1
                if cnt <= 0:
                    break
            cur_color = next(generator)
            if cur_color == self.__color:
                raise Exception(f"Последовательность смены режимов нарушена ({self.__color} == {cur_color[0]}) " +
                                f"Цвета не могут повторяться, проверьте последовательность {self.__traffic_order}!")
            self.__color = cur_color


# С ошибкой нарушения порядка режимов
tl1 = TrafficLight('red', traffic_order=('red', 'yellow', 'green', 'red'), traffic_timeouts={'red': 2, 'yellow': 2, 'green': 2})
try:
    tl1.running()
except Exception as e:
    print(e)
print("")
# С ограничением смены режимов
tl2 = TrafficLight('green', color_change_count=10)
tl2.running()

# 2. Реализовать класс Road (дорога).
#
#     определить атрибуты: length (длина), width (ширина);
#     значения атрибутов должны передаваться при создании экземпляра класса;
#     атрибуты сделать защищёнными;
#     определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#     использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
#     толщиной в 1 см*число см толщины полотна;
#     проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    _length = 0
    _width = 0
    __weight = 100.22

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def _calculate_asphalt_weight(self, height):
        return self._length * self._width * self.__weight * height

    def print_asphalt_weight(self, height):
        print(f"Масса асфальта, необходимого для покрытия дороги длиной {self._length} м шириной {self._width} м " +
              f"и высотой {height} см равна {self._calculate_asphalt_weight(height):10.2f} кг")
        print(f"{self._length} м * {self._width} м * {self.__weight} кг * {height} см = " +
              f"{self._calculate_asphalt_weight(height)/1000:10.2f} т")


r = Road(1000, 100)
r.print_asphalt_weight(12)
print(f"Проверка: {1000 * 100 * 100.22 * 12:10.2f} кг => {1000 * 100 * 100.22 * 12 / 1000:10.2f} т")

# 3. Реализовать базовый класс Worker (работник).
#
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
#     {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#     и дохода с учётом премии (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
#     проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        if isinstance(income, dict) and len(income.keys()) > 0:
            self._income = income


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_name_with_position(self):
        return f"{self.name} {self.surname} - {self.position}"

    def get_total_income(self):
        s = 0
        for i in self._income.keys():
            s += self._income[i]
        return s


p1 = Position("Petr", "Petrov", "Worker", {"wage": 50000.00, "bonus": 123.22, "penalty": -10.02})
print(p1.get_full_name())
print(f"{p1.get_full_name_with_position()} Доход: {p1.get_total_income():10.2f} p")
print(f"{p1.name} {p1.surname} - {p1.position}; Доход: {p1.get_total_income():10.2f} p")
print("")
p2 = Position("Ivan", "Ivanov", "Accountant", {"wage": 100000.00, "bonus": 123.22, "penalty": -110.22})
print(p2.get_full_name())
print(f"{p2.get_full_name_with_position()} Доход: {p2.get_total_income():10.2f} p")
print(f"{p2.name} {p2.surname} - {p2.position}; Доход: {p2.get_total_income():10.2f} p")


# 4. Реализуйте базовый класс Car.
#
#     у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#     А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#     опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#     добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#     для классов TownCar и WorkCar переопределите метод show_speed.
#     При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    name = ""
    model = ""
    speed = 0
    __max_speed = 0
    color = "Black"
    _is_police = False

    def __init__(self, name, model, speed, color):
        self.name = name
        self.model = model
        self.speed = speed
        self.color = color

    def go(self):
        print("Движение вперед")

    def go_back(self):
        print("Движение назад")

    def stop(self):
        print("Остановка")

    def turn(self, direction):
        print(f"Поворот {direction}")

    def show_speed(self):
        if 0 < self.__max_speed < self.speed:
            print(f"Превышение скорости! Максимальная скорость {self.speed} км/ч. Ваша скорость = {self.speed} км/ч")
        else:
            print(f"Скорость = {self.speed} км/ч")

    def __str__(self):
        return f"{self.name} {self.model} speed: {self.speed} км/ч{' - полицейская машина' if self._is_police else ''}"

class TownCar(Car):
    __max_speed = 60

    @property
    def max_speed(self):
        return self.__max_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    __max_speed = 40

    @property
    def max_speed(self):
        return self.__max_speed


class PoliceCar(Car):
    def __init__(self, name, model, speed, color):
        super().__init__(name, model, speed, color)
        self._is_police = True


t = TownCar("Hundai", "Sonata", 100, "White")
print(t.__class__)
print(t)
print(f"Ограничение скорости = {t.max_speed}")
t.go()
t.turn("направо")
t.go()
t.stop()
print("")

s = SportCar("Porsche", "Pnamera", 300, "White")
print(s.__class__)
print(s)
s.go()
s.stop()
print("")

w = WorkCar("KIA", "Stinger", 300, "White")
print(w.__class__)
print(w)
print(f"Ограничение скорости = {w.max_speed}")
w.go()
w.turn("налево")
t.go()
w.stop()
print("")

p = PoliceCar("ВАЗ", "2110", 300, "White")
print(p.__class__)
print(p)
p.go()
p.turn("на разворот")
p.stop()
p.go_back()
p.stop()
print("")


# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
#     определить в нём атрибут title (название) и метод draw (отрисовка).
#     Метод выводит сообщение «Запуск отрисовки»;
#     создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#     в каждом классе реализовать переопределение метода draw.
#     Для каждого класса метод должен выводить уникальное сообщение;
#     создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    """канцелярская принадлежность"""
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

    def __str__(self):
        print(self.title)


class Pen(Stationery):
    """ручка"""
    def draw(self):
        print(f"{self.title}  ({self.__doc__}) - запуск отрисовки")


class Pencil(Stationery):
    """карандаш"""
    def draw(self):
        print(f"{self.title}  ({self.__doc__}) - запуск отрисовки")


class Handle(Stationery):
    """маркер"""
    def draw(self):
        print(f"{self.title}  ({self.__doc__}) - запуск отрисовки")


pen = Pen("Parker")
print(pen.__class__)
print(f"{pen.title} - {pen.__doc__}")
pen.draw()
print("")
pencil = Pencil("Derevyashko")
print(pencil.__class__)
print(f"{pencil.title} - {pencil.__doc__}")
pencil.draw()
print("")
handle = Handle("Markeritto")
print(handle.__class__)
print(f"{handle.title} - {handle.__doc__}")
handle.draw()
