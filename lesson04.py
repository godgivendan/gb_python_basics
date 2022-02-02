from sys import argv
from argparse import ArgumentParser, ArgumentTypeError, ArgumentError
from functools import reduce
from itertools import count, cycle

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
print("==================== 1.1 argv ====================")


def calculate_salary(rate_per_hour_: float, work_hours_: float, premium_: float):
    return (work_hours_ * rate_per_hour_) + premium_


try:
    script_name, rate_per_hour, work_hours, premium = argv
    print(f"script_name: {script_name}")
    print("Данные для расчета заработной платы:")
    print(f"Ставка в час = {rate_per_hour}")
    print(f"Выработка в часах = {work_hours}")
    print(f"Премия = {premium}")
    sm = calculate_salary(float(rate_per_hour), float(work_hours), float(premium))
except ValueError as e:
    print('Для запуска расчета зп укажите числовые параметры в следующем порядке ' +
          'rate_per_hour(ставка в час), work_hours(выработка в часах), premium(премия), разделенные пробелами.')
except Exception as e:
    print('Для запуска расчета зп укажите числовые параметры в следующем порядке ' +
          'rate_per_hour(ставка в час), work_hours(выработка в часах), premium(премия), разделенные пробелами.')
    print(e)
else:
    print("Рассчет:")
    print(f"Формула: ({work_hours} * {rate_per_hour}) + {premium} = {sm}")
    print(f"Заработная плата сотрудника состовляет {sm}")
finally:
    print("==================== end ====================")


print("==================== 1.2 argparse ====================")
parser = ArgumentParser(description="Расчет заработной платы сотрудника")
parser.add_argument('--work_hours', help="Выработка в часах", type=float, default=0) # Сделан необязательным для запуска скрипта в общем блоке
parser.add_argument('--rate_per_hour', '-rph', help="Ставка в час", type=float, default=100)
parser.add_argument('--premium', '-p', help="Премия", type=float, default=0)
# print(parser.format_help())
try:
    args = parser.parse_args()
    print(args)
    script_name = parser.prog
    print(f"script_name: {script_name}")
    print("Данные для расчета заработной платы:")
    print(f"Ставка в час = {args.rate_per_hour}")
    print(f"Выработка в часах = {args.work_hours}")
    print(f"Премия = {args.premium}")
    sm = calculate_salary(float(args.rate_per_hour), float(args.work_hours), float(args.premium))
except ValueError as e:
    print('Для запуска расчета зп укажите параметры в следующем формате: ' +
          ' lesson04_script_named_params.py [-h] [--rate_per_hour RATE_PER_HOUR] [--premium PREMIUM] work_hours.')
    print(e)
except ArgumentTypeError as e:
    print('Для запуска расчета зп укажите параметры в следующем формате: ' +
          ' lesson04_script_named_params.py [-h] [--rate_per_hour RATE_PER_HOUR] [--premium PREMIUM] work_hours.')
    print(e)
except ArgumentError as e:
    print('Для запуска расчета зп укажите параметры в следующем формате: ' +
          ' lesson04_script_named_params.py [-h] [--rate_per_hour RATE_PER_HOUR] [--premium PREMIUM] work_hours.')
    print(e)
except Exception as e:
    print('Для запуска расчета зп укажите параметры в следующем формате: ' +
          ' lesson04_script_named_params.py [-h] [--rate_per_hour RATE_PER_HOUR] [--premium PREMIUM] work_hours.')
    print(e)
else:
    print("Рассчет:")
    print(f"Формула: ({args.work_hours} * {args.rate_per_hour} р.) + {args.premium} р. = {sm} р.")
    print(f"Заработная плата сотрудника состовляет {sm} р.")
    pass
finally:
    print("==================== end ====================")

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
print("==================== 2 ====================")


def generate_res_nums_yield(ns):
    prev_el = None
    for el in ns:
        if prev_el is not None and el > prev_el:
            yield el
        prev_el = el


def generate_res_nums_gnrtr(ns):
    g_nums = (el for el in ns)
    next(g_nums)
    prev_g_nums = (el for el in ns)
    return (el for el in g_nums if el > next(prev_g_nums))


nums = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
while True:
    try:
        nms = input('Введите список чисел разделенных пробелами (Enter - cписок по умолчанию): ').split()
        if len(nms) > 0:
            nums = [int(el) for el in nms]
        break
    except Exception as e:
        print('Вы ввели неверное значение! Введенный Вами список содержит некорректные данные! Попробуйте снова.')
        # print(e)

print(f"Изначальный массив: {nums}")
print(f"Результат по методу 1: {list(generate_res_nums_yield(nums))}")
print(f"Результат по методу 2: {list(generate_res_nums_gnrtr(nums))}")


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
print("==================== 3 ====================")
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
print("==================== 4 ====================")


def generate_distinct_nums_yield(ns):
    for el in ns:
        if len([el1 for el1 in ns if el1 == el]) == 1:
            yield el


def generate_distinct_nums_set(ns):
    return [el for el in ns if ns.count(el) == 1]


nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
while True:
    try:
        nms = input('Введите список чисел разделенных пробелами (Enter - cписок по умолчанию): ').split()
        if len(nms) > 0:
            nums = [int(el) for el in nms]
        break
    except Exception as e:
        print('Вы ввели неверное значение! Введенный Вами список содержит некорректные данные! Попробуйте снова.')
        # print(e)

print(f"Изначальный массив: {nums}")
print(f"Результат по методу 1: {list(generate_distinct_nums_yield(nums))}")
print(f"Результат по методу 2: {generate_distinct_nums_set(nums)}")


# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
print("==================== 5 ====================")


def multiply_els(prev_el, el):
    return prev_el * el


lst = [el for el in range(100, 1001) if el % 2 == 0]
print(lst)
print(f" Произведение: {reduce(multiply_els, lst)}")
print(f" Сумма: {reduce(lambda prev_el, el: prev_el + el, lst)}")


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
print("==================== 6.1 a ====================")
parser = ArgumentParser(description="Пример работы функции itertools.count()")
parser.add_argument('--min_digit', help="Начальное целое число для перебора", type=int, default=1) # Сделан необязательным для запуска скрипта в общем блоке
parser.add_argument('--max_digit', '-rc', help="Максимальное целое число для перебора", type=int, default=20)
# print(parser.format_help())

try:

    args = parser.parse_args()
    print(args)
    script_name = parser.prog
    print(f"script_name: {script_name}")
    print("Данные для запуска примера работы функции itertools.count():")
    print(f"Начальное целое число для перебора = {args.min_digit}")
    print(f"Максимальное целое число для перебора = {args.max_digit}")
except ValueError as e:
    print('Для запуска примера работы функции itertools.count() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    # print(e)
except ArgumentTypeError as e:
    print('Длязапуска примера работы функции itertools.count() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    # print(e)
except ArgumentError as e:
    print('Для запуска примера работы функции itertools.count() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    # print(e)
except Exception as e:
    print('Для запуска примера работы функции itertools.count() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    # print(e)
else:
    print("Результат: ", end="")
    for el in count(args.min_digit):
        print(el, end="")
        if el < args.max_digit:
            print(", ", end="")
        else:
            print("")
            break
finally:
    print("==================== end ====================")

print("==================== 6.2 b ====================")
parser = ArgumentParser(description="Пример работы функции itertools.cycle()")
parser.add_argument('--str_data', help="Строковая последовательность для перебора", type=str, default='ABC') # Сделан необязательным для запуска скрипта в общем блоке
parser.add_argument('--repeat_count', '-rc', help="Количество символов для перебора", type=int, default=3)
# print(parser.format_help())

try:
    args = parser.parse_args()
    print(args)
    script_name = parser.prog
    print(f"script_name: {script_name}")
    print("Данные для запуска примера работы функции itertools.cycle():")
    print(f"Строковая последовательность для перебора = {args.str_data}")
    print(f"Количество символов для перебора = {args.repeat_count}")
except ValueError as e:
    print('Для запуска примера работы функции itertools.cycle() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    print(e)
except ArgumentTypeError as e:
    print('Длязапуска примера работы функции itertools.cycle() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    print(e)
except ArgumentError as e:
    print('Для запуска примера работы функции itertools.cycle() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    print(e)
else:
    print("Результат: ", end="")
    c = args.repeat_count
    for el in cycle(args.str_data):
        print(el, end="")
        c -= 1
        if c > 0:
            print(", ", end="")
        else:
            print("")
            break
finally:
    print("==================== end ====================")

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
print("==================== 7 ====================")


def fact(n):
    f = 1
    for nm in range(1, n+1):
        f *= nm
        yield nm, f


n = 4
while True:
    try:
        nm = input('Введите целое число > 0 (Enter - число по умолчанию = 4): ')
        if nm != '' and abs(int(nm)) > 0:
            n = abs(int(nm))
        break
    except Exception as e:
        print('Вы ввели неверное значение! Попробуйте снова.')
        # print(e)
f = 0
f1 = 1 # другой вариант
print(f"{n}! = ", end="")
for el, elf in fact(n):
    f = elf
    f1 *= el # другой вариант
    if el > 1:
        print(" * ", end="")
    print(f"{el}", end="")
print(f" = {f}")
print(f"{n}! = {f1}") # другой вариант


















