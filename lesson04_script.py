# -*- coding: utf-8 -*-
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

print("==================== 1 ====================")


def calculate_salary(rate_per_hour, work_hours, premium):
    return (work_hours * rate_per_hour) + premium


try:
    script_name, rate_per_hour, work_hours, premium = argv
    print(f"script_name: {script_name}")
    print("Данные для расчета заработной платы:")
    print(f"Ставка в час = {rate_per_hour}")
    print(f"Выработка в часах = {work_hours}")
    print(f"Премия = {premium}")
    sm = calculate_salary(float(rate_per_hour), float(work_hours), float(premium))
except ValueError as e:
    print('Для запуска расчета зп укажите числовые параметры в следующем порядке rate_per_hour(ставка в час), work_hours(выработка в часах), premium(премия), разделенные пробелами.')
else:
    print("Рассчет:")
    print(f"Формула: ({work_hours} * {rate_per_hour}) + {premium} = {sm}")
    print(f"Заработная плата сотрудника состовляет {sm}")
finally:
    print("==================== end ====================")


