# -*- coding: utf-8 -*-
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from argparse import ArgumentParser, ArgumentTypeError, ArgumentError

print("==================== 1 ====================")
parser = ArgumentParser(description="Расчет заработной платы сотрудника")
parser.add_argument('work_hours', help="Выработка в часах", type=float, default=0)
parser.add_argument('--rate_per_hour', '-rph', help="Ставка в час", type=float, default=100)
parser.add_argument('--premium', '-p', help="Премия", type=float, default=0)
# print(parser.format_help())


def calculate_salary(rate_per_hour_: float, work_hours_: float, premium_: float):
    return (work_hours_ * rate_per_hour_) + premium_


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
else:
    print("Рассчет:")
    print(f"Формула: ({args.work_hours} * {args.rate_per_hour} р.) + {args.premium} р. = {sm} р.")
    print(f"Заработная плата сотрудника состовляет {sm} р.")
finally:
    print("==================== end ====================")
