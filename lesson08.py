import re
from abc import ABC
from datetime import datetime
import random


class RegExException(Exception):
    pass


class DateValueException(ValueError):
    pass


class DuplicateException(ValueError):
    pass


class ItemNotFoundException(ValueError):
    pass


class InputUtils:
    @staticmethod
    def get_input_element(message, tp):
        while True:
            try:
                n = tp(input(message + ': '))
                break
            except Exception as e:
                print('Вы ввели неверное значение! Попробуйте снова.')
                # print(e)
        return n


# 1. Реализовать класс «Дата»,функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
print("")
print("====================== 1 ======================")


class Date:
    """Дата"""
    def __init__(self, dt: str):
        if self.check_date(dt):
            self.dt = dt
        else:
            raise RegExException("Введите дату в формате dd-mm-yyyy!")

    @classmethod
    def date_to_int_tuple(cls, dte: str):
        try:
            # Другой способ
            dto = datetime.strptime(dte, '%d-%m-%Y')
            return dto.day, dto.month, dto.year
        except Exception as e:
            raise DateValueException(f"Формат даты неверен: {e}")

    @classmethod
    def strdate_to_int_tuple(cls, dte: str):
        try:
            d, m, y = dte.split('-')
            return int(d), int(m), int(y)
        except Exception as e:
            raise DateValueException(f"Формат даты неверен: {e}")

    @staticmethod
    def check_date(dte):
        if re.match(r"^([0-2][0-9]|(3)[0-1])-(((0)[0-9])|((1)[0-2]))-\d{4}$", dte):
            d, m, y = Date.date_to_int_tuple(dte)
            if 1 <= d <= 31 and 1 <= m <= 12 and 2000 <= y <= 2022:
                return True
        return False


dt = "01-01-2022"
print(f"Дата {dt} {'верна.' if Date.check_date(dt) else 'неверна!'}")
try:
    d1 = Date(dt)
    d, m, y = d1.strdate_to_int_tuple(dt)
    print(f"1. Число: {d}; Месяц: {m}; Год: {y}")
    d, m, y = d1.date_to_int_tuple(dt)
    print(f"2. Число: {d}; Месяц: {m}; Год: {y}")
except RegExException as e:
    print(e)
except DateValueException as e:
    print(e)
except Exception as e:
    print(e)

dt = "01.01.2022"
try:
    d2 = Date(dt)
except RegExException as e:
    print(e)
except Exception as e:
    print(e)
try:
    d, m, y = Date.strdate_to_int_tuple(dt)
    print(f"Число: {d}; Месяц: {m}; Год: {y}")
except DateValueException as e:
    print(e)
try:
    d, m, y = Date.date_to_int_tuple(dt)
    print(f"Число: {d}; Месяц: {m}; Год: {y}")
except DateValueException as e:
    print(e)

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.
print("")
print("====================== 2 ======================")


class ZeroDivErr(ZeroDivisionError):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

    @classmethod
    def divide(cls, el1, el2):
        if el2 is None or el2 == 0:
            raise ZeroDivErr("Деление на 0 запрещено!")
        return el1 / el2

    def __str__(self):
        return "Ошибка деления на ноль: "+self.message


while True:
    a = InputUtils.get_input_element('Введите числитель', int)
    b = InputUtils.get_input_element('Введите знаменатель', int)
    try:
        print(ZeroDivErr.divide(a, b))
    except ZeroDivErr as e:
        print(f"!!! {e} !!!")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)

    ans = input('Повторить (yes/no)? To proceed press enter: ')
    if ans != '' and ans.lower() != 'yes':
        break

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
# (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
print("")
print("====================== 3 ======================")


class ArrayOnlyListErr(Exception):
    @classmethod
    def validate(cls, checklist):
        for elt in checklist:
            if not isinstance(elt, int) and not isinstance(elt, float):
                raise ArrayOnlyListErr("Список должен содержать только числа!")

    @classmethod
    def append(cls, appendlist, appendelt):
        try:
            appendlist.append(int(appendelt))
        except Exception as e:
            raise ArrayOnlyListErr("Список должен содержать только числа!")
        return appendlist


lst = []
while True:
    try:
        print(ArrayOnlyListErr.append(lst, InputUtils.get_input_element('Введите число', int)))
        ArrayOnlyListErr.validate(lst)
        print(f"Текуший список: {lst}")
    except ArrayOnlyListErr as e:
        print(f"Ошибка: ({e})")
    except Exception as e:
        print(e)

    ans = input('Добавить еще элемент (yes/no)? To proceed press enter: ')
    if ans != '' and ans.lower() != 'yes':
        break
print(f"Результирующий список: {lst}")

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
print("")
print("====================== 4 ======================")


class Equipment:
    """Оргтехника"""
    __cnt = 0
    __equipment_list = {}

    def __init__(self, name: str, model: str, color: str):
        self.name = name
        self.model = model
        self.color = color
        Equipment.__cnt += 1
        # create equipment ID
        hsh = random.getrandbits(128)
        while hsh is None or hsh in self.__equipment_list:
            hsh = random.getrandbits(128)
        self.__id = hsh
        # add equipment to warehouse_list
        self.__equipment_list[hsh] = f"{hsh:<40} - {self.name} {self.model}"

    def do_action(self):
        print("Doing something...")

    @property
    def id(self):
        return self.__id

    @classmethod
    def equipment_list(cls):
        return cls.__equipment_list

    @classmethod
    def cnt(cls):
        return cls.__cnt

    def __str__(self):
        return f"{self.name} {self.model} (ID: {self.__id}; Color: {self.color})"


class Printer(Equipment):
    """Принтеры"""
    __cnt = 0

    def __init__(self, name: str, model: str, color: str, print_speed: int, paper_format: str):
        super().__init__(name, model, color)
        self.print_speed = print_speed
        self.paper_format = paper_format
        Printer.__cnt += 1

    def do_action(self):
        self.print_papers(self.print_speed, self.paper_format)

    @classmethod
    def print_papers(cls, print_speed, paper_format):
        print(f"{cls}: Печать страниц {paper_format} со скоростью {print_speed} страниц в минуту...")

    @classmethod
    def cnt(cls):
        return cls.__cnt


class Scanner(Equipment):
    """Сканеры"""
    __cnt = 0

    def __init__(self, name: str, model: str, color: str, scan_speed: int, paper_format: str):
        super().__init__(name, model, color)
        self.scan_speed = scan_speed
        self.paper_format = paper_format
        Scanner.__cnt += 1

    def do_action(self):
        self.print_papers(self.print_speed, self.paper_format)

    @classmethod
    def scan_papers(cls, print_speed, paper_format):
        print(f"{cls}: Сканирование страниц {paper_format} со скоростью {print_speed} страниц в минуту...")

    @classmethod
    def cnt(cls):
        return cls.__cnt


class Xerox(Equipment):
    """Ксероксы"""
    __cnt = 0

    def __init__(self, name: str, model: str, color: str, copy_speed: int, paper_format: str):
        super().__init__(name, model, color)
        self.copy_speed = copy_speed
        self.paper_format = paper_format
        Xerox.__cnt += 1

    def do_action(self):
        self.print_papers(self.print_speed, self.paper_format)

    @classmethod
    def copy_papers(cls, print_speed, paper_format):
        print(f"{cls}: Ксерокопирование страниц {paper_format} со скоростью {print_speed} страниц в минуту...")

    @classmethod
    def cnt(cls):
        return cls.__cnt


p1 = Printer('Printer HP', 'HP1001', 'black', 12, 'A4')
p2 = Printer('Printer Canon', 'NW1234', 'white', 13, 'A4')
p3 = Printer('Printer HP', 'HP51231', 'gray', 13, 'A4')
p4 = Printer('Printer Canon', 'P20231', 'blue', 13, 'A4')
p5 = Printer('Printer HP', 'HP1331', 'white', 13, 'A4')
p6 = Printer('Printer Canon', 'N4231', 'black', 13, 'A4')
p7 = Printer('Printer Benq', 'BQ123111', 'black', 13, 'A4')

s1 = Scanner('Scanner HP', 'S131213', 'gray', 5, 'A4')
s2 = Scanner('Scanner Cannon', 'NS213', 'red', 5, 'A4')
s3 = Scanner('Scanner Samsung', 'S41213', 'blue', 5, 'A4')
s4 = Scanner('Scanner Benq', 'BQ131213', 'green', 5, 'A4')

x1 = Xerox('Xerox HP', 'S131112', 'dark gray', 25, 'A4')
x2 = Xerox('Xerox Canon', 'NX4512', 'dark gray', 25, 'A4')
x3 = Xerox('Xerox Benq', 'BQ13432', 'dark gray', 25, 'A4')
x4 = Xerox('Xerox HP', 'S3112', 'dark gray', 25, 'A4')
x5 = Xerox('Xerox Benq', 'BQ7931', 'dark gray', 25, 'A4')
print("")
print("=======================================")
print(f"Общее количество принтеров:  {Printer.cnt():>10}")
print(f"Общее количество сканеров:   {Scanner.cnt():>10}")
print(f"Общее количество крероксов:  {Xerox.cnt():>10}")
print("=======================================")
print(f"Общее количество оргтехники: {Equipment.cnt():>10}")
print("=======================================")
print("")
print("========================= Cписок оргтехники ===========================")
for eq_id, eq_name in Equipment.equipment_list().items():
    print(eq_name)
print("=======================================================================")

# 5 и 6 объеденены

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
print("")
print("====================== 4 + 5 + 6 ======================")


class BusinessUnit:
    """Бизнес еденица организации"""
    __cnt = 0
    __business_unit_equipment_list = {}
    __messages = {
        "reg_err": "Оборудование с ID {id} уже зарегистрировано в данной бизнес еденице!",
        "reg_other_err": "Оборудование с ID {id} уже зарегистрировано в другой бизнес еденице {b_units}!",
        "eq_not_found_err": "Оборудование с ID {id} не найдено в данной бизнес еденице!",
        "del_err": "Удаление бизнес еденицы запрещено! За данной бизнес еденицей закреплена оргтехника."
    }

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__cnt += 1  # BusinessUnit
        # create warehouse ID
        hsh = random.getrandbits(128)
        while hsh is None or hsh in self.__business_unit_equipment_list:
            hsh = random.getrandbits(128)
        self.__id = hsh
        self.get_or_create_business_unit_equipment_if_not_exists(self)

    def append_equipment(self, remove_in_other: bool, check_in_other: bool, *eqs):
        """
        Прием оборудования
        :param remove_in_other: Автоудаление указанного оборудования в других бизнес еденицах организации
        :param check_in_other: Проверка наличия указанного оборудования в других бизнес еденицах организации (вызов ошибки)
        :param eqs: Экземпляры оборудования/оргтехники
        :return: Словарь с оборудованием в текущей бизнес еденице организации
        """
        bu_eq = self.get_or_create_business_unit_equipment_if_not_exists(
            self)  # self.__business_unit_equipment_list[self.__id]
        for eq in eqs:
            if eq.id in bu_eq:
                # "Оборудование с ID {id} уже зарегистрировано в данной бизнес еденице!"
                raise DuplicateException(self.get_message('reg_err').format(id=eq.id))
            if check_in_other:
                b_units = self.check_equipment(eq.id)
                if len(b_units) > 0:
                    # "Оборудование с ID {id} уже зарегистрировано в другой бизнес еденице {b_units}!"
                    raise DuplicateException(self.get_message('reg_other_err').format(id=eq.id, b_units=b_units))
        for eq in eqs:
            bu_eq[eq.id] = eq
            if remove_in_other:
                self.remove_equipment_in_other_business_units(eq.id, self.__id)
        return bu_eq

    def remove_equipment(self, *eqs):
        """
        Открепление оборудования
        :param eqs: Экземпляры оборудования/оргтехники
        :return: Словарь с оборудованием в бизнес еденице
        """
        weq = self.get_or_create_business_unit_equipment_if_not_exists(self)
        for eq in eqs:
            if eq.id not in weq:
                # "Оборудование с ID {eq.id} не найдено в данной бизнес еденице!"
                raise ItemNotFoundException(self.get_message('eq_not_found_err').format(id=eq.id))
        for eq in eqs:
            weq.pop(eq.id)
        return weq

    def remove_all_equipment(self):
        """
        Открепление всего оборудования в бизнес еденице
        :return: Словарь с оборудованием в бизнес еденице
        """
        weq = self.get_or_create_business_unit_equipment_if_not_exists(self)
        for eqv_id, eqv_name in weq.items():
            if eqv_id != 'name':
                # print(eqv_name)
                weq.pop(eqv_id)
        # weq = {'name': f"{self.__id:<40} - {self.name}"}
        return weq

    @classmethod
    def get_or_create_business_unit_equipment_if_not_exists(cls, bisiness_unit):
        """
        Получение/Создание списка оборудования в бизнес еденице
        :param bisiness_unit: Эксемпляр бизнес еденицы
        :return: Справочник оборудования
        """
        if bisiness_unit.__id not in cls.__business_unit_equipment_list:
            cls.__business_unit_equipment_list[bisiness_unit.__id] = {
                'name': f"{bisiness_unit.__id:<40} - {bisiness_unit.name}"}
        return cls.__business_unit_equipment_list[bisiness_unit.__id]

    @classmethod
    def check_equipment(cls, equipment_id):
        """
        Проверка наличия указанного оборудования в других бизнес еденицах
        :param equipment_id: ИД оборудования
        :return: Список бизнес едениц
        """
        b_units = []
        for b_unit_id, b_unit_dict in cls.__business_unit_equipment_list.items():
            if equipment_id in b_unit_dict:
                b_units.append(b_unit_id)
        return b_units

    @classmethod
    def remove_equipment_in_other_business_units(cls, equipment_id, business_unit_id):
        """
        Автоудаление указанного оборудования в других балансовых еденицах
        :param equipment_id: ИД оборудования
        :param business_unit_id: ИД бизнес еденицы-исключения (где удалять не нужно)
        :return: True
        """
        for bunit_id, bunit_dict in cls.__business_unit_equipment_list.items():
            if bunit_id != business_unit_id:
                if equipment_id in bunit_dict:
                    bunit_dict.pop(equipment_id)
        return True

    @classmethod
    def business_unit_equipment_list(cls):
        return cls.__business_unit_equipment_list

    @property
    def id(self):
        return self.__id

    @classmethod
    def get_message(cls, msg_id):
        return cls.__messages[msg_id]

    def __del__(self):
        bu_eq = dict(self.get_or_create_business_unit_equipment_if_not_exists(self))  # BusinessUnit
        # Закоментировал, чтобы не вылетало сообщение об ошибке, при удалении экземпляров
        # if len(weq.items()) > 1:
        #     # "Удаление бизнес еденицы запрещено! За данной бизнес еденицей закреплена оргтехника."
        #     raise Exception(self.get_message('del_err'))
        self.__business_unit_equipment_list.pop(self.__id)  # BusinessUnit


class Warehouse(BusinessUnit):
    """Cклад организации"""
    __messages = {
        "reg_err": "Оборудование с ID {id} уже зарегистрировано на данном складе!",
        "reg_other_err": "Оборудование с ID {id} уже зарегистрировано в другом филиале/складе {b_units}!",
        "eq_not_found_err": "Оборудование с ID {id} не найдено в данном складе!",
        "del_err": "Удаление склада запрещено! За данным складом закреплена оргтехника."
    }

    @classmethod
    def get_message(cls, msg_id):
        return cls.__messages[msg_id]




class Branch(BusinessUnit):
    """Филиал организации"""
    __messages = {
        "reg_err": "Оборудование с ID {id} уже зарегистрировано в данном филиале!",
        "reg_other_err": "Оборудование с ID {id} уже зарегистрировано в другом филиале/складе {b_units}!",
        "eq_not_found_err": "Оборудование с ID {id} не найдено в данном филиале!",
        "del_err": "Удаление филиала запрещено! За данным филиалом закреплена оргтехника."
    }

    @classmethod
    def get_message(cls, msg_id):
        return cls.__messages[msg_id]


class Organization:
    """Организация"""
    __business_units = {}

    def __init__(self, name, *b_units):
        self.name = name
        for bu in b_units:
            if isinstance(bu, BusinessUnit):
                self.__business_units[bu.id] = bu

    def append_business_units(self, *b_units):
        for bu in b_units:
            if isinstance(bu, BusinessUnit):
                self.__business_units[bu.id] = bu
        return self.__business_units

    def remove_business_units(self, *b_units):
        for bu in b_units:
            if isinstance(bu, BusinessUnit):
                self.__business_units.pop(bu.id)
        return self.__business_units

    @classmethod
    def business_unit_list(cls):
        return cls.__business_units

    def print_business_units_list(self):
        print("")
        print(f"{self.name:^35}")
        print("===== Cписок филиалов/складов =====")
        for bu_id, bu in self.__business_units.items():
            print(f"{bu.name}")
        print("===================================")

    def __del__(self):
        self.__business_units = {}


w1 = Warehouse('Warehouse 1', 'Address 1')
w2 = Warehouse('Warehouse 2', 'Address 2')

b1 = Warehouse('Branch 1', 'Address 3')
b2 = Warehouse('Branch 2', 'Address 4')

o = Organization("Organization 1", b1, b2, w1, w2)
o.print_business_units_list()

print("")
print("=========================== Операции с филиалами/складами =============================")
w1.append_equipment(False, True, p1, s1, x1)  # прием
w2.append_equipment(False, True, p2)  # прием
w2.remove_equipment(p2)  # отерепление/выдача
w2.append_equipment(False, True, p2, p7)  # прием
w2.append_equipment(True, False, p1)  # перемещение

b1.append_equipment(True, False, p5, p6, s3, x2, x3)  # прием
b2.append_equipment(True, False, p3, p4, s2, s4, x4, x5)  # прием

try:
    w2.append_equipment(False, True, x1)  # прием с ошибкой, т.к. оборудование закреплено за другим складом
except Exception as e:
    print(e)

print("")
print("=========== Оборудование в филиалах/на складах ===========")
for w_id, w_dict in BusinessUnit.business_unit_equipment_list().items():
    print("-----------------------------------------------")
    print(f"{w_dict['name'].split(' - ')[1]}")
    print("-----------------------------------------------")
    cnt_types = {}
    for eq_id, eq_obj in w_dict.items():
        if eq_id != 'name':
            if eq_obj.__class__.__doc__ not in cnt_types:
                cnt_types[eq_obj.__class__.__doc__] = 0
            cnt_types[eq_obj.__class__.__doc__] = cnt_types[eq_obj.__class__.__doc__] + 1
            # print(f"{eq_obj}")
    for eqtype_id, eqtype_cnt in cnt_types.items():
        print(f"{eqtype_id:<31} {eqtype_cnt:>13}")
print("===============================================")

print("")
print("=========================== Cписок оборудования в филиалах/на складах =============================")
for w_id, w_dict in BusinessUnit.business_unit_equipment_list().items():
    print("----------------------------------------------------------------------------------------")
    print(f"{w_dict['name']}")
    print("----------------------------------------------------------------------------------------")
    for eq_id, eq_obj in w_dict.items():
        if eq_id != 'name':
            print(f"{eq_obj}")

print("========================================================================================")

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.
print("")
print("====================== 7 ======================")


class ComplexNumber:
    """Комплексное число"""

    def __init__(self, a: float, b: float):
        self._a = a  # Вещественная часть
        self._b = b  # Мнимая часть

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def type(self):
        if self._a == 0 and self._b != 0:
            return "Мнимое число"
        elif self._a != 0 and self._b == 0:
            return "Вещественное число"
        return "Комплексное число"

    def __add__(self, other):
        return ComplexNumber(
            self.a + other.a,
            self.b + other.b
        )

    def __sub__(self, other):
        return ComplexNumber(
            self.a - other.a,
            self.b - other.b
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.a * other.a - self.b * other.b,
            self.b * other.a + self.a * other.b
        )

    def __truediv__(self, other):
        return ComplexNumber(
            round(self.a * other.a + self.b * other.b, 20) / round((other.a**2) + (other.b**2), 20),
            round(self.b * other.a - self.a * other.b, 20) / round((other.a**2) + (other.b**2), 20)
        )

    def __str__(self):
        return f"({self._a}{'+' if self._b > 0 else '-'}{abs(self._b)}j)"


print("")
print("==== Комплексные числа ====")
c1 = ComplexNumber(13, 14)
c_1 = complex(13, 14)
print(f"{c1} ---> {c_1}")
c2 = ComplexNumber(2, 9)
c_2 = complex(2, 9)
print(f"{c2} ---> {c_2}")
print("==== Сложение ====")
c3 = c1 + c2
c_3 = c_1 + c_2
print(f"{c1} + {c2} = {c3}")
print(f"{c_1} + {c_2} = {c_3}")
print("==== Вычитание ====")
c3 = c1 - c2
c_3 = c_1 - c_2
print(f"{c1} - {c2} = {c3}")
print(f"{c_1} - {c_2} = {c_3}")
print("==== Умножение ====")
c3 = c1 * c2
c_3 = c_1 * c_2
print(f"{c1} * {c2} = {c3}")
print(f"{c_1} * {c_2} = {c_3}")
print("==== Деление ====")
c3 = c1 / c2
c_3 = c_1 / c_2
print(f"{c1} / {c2} = {c3}")
print(f"{c_1} / {c_2} = {c_3}")












