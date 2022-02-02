from argparse import ArgumentParser, ArgumentTypeError, ArgumentError
from itertools import cycle

print("==================== 6.2 ====================")
parser = ArgumentParser(description="Пример работы функции itertools.cycle()")
parser.add_argument('str_data', help="Строковая последовательность для перебора", type=str, default='ABC')
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
