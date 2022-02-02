from argparse import ArgumentParser, ArgumentTypeError, ArgumentError
from itertools import count

print("==================== 6.1 ====================")
parser = ArgumentParser(description="Пример работы функции itertools.count()")
parser.add_argument('min_digit', help="Начальное целое число для перебора", type=int, default=1)
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
    print(e)
except ArgumentTypeError as e:
    print('Длязапуска примера работы функции itertools.count() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    print(e)
except ArgumentError as e:
    print('Для запуска примера работы функции itertools.count() укажите параметры в следующем формате: ' +
          ' lesson04_script_cycle.py [-h] [--repeat_count REPEAT_COUNT] str_data.')
    print(e)
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
