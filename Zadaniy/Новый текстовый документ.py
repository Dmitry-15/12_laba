#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Найти среднее арифметическое чисел, их сумму
и наибольшее значение словаря.
"""


def arithmetic(**kwargs):
    x = 0
    max_val = max(kwargs.values())
    len_of = len(kwargs)
    for numbers in kwargs.values():
        x += float(numbers)
    print(f"Cумма чисел: {x}")
    sum_of = x / len_of
    print('Среднее арифметическое чисел: ', sum_of)
    for k, v in kwargs.items():
        if v == max_val:
            print(f"Наибольшая переменная {k} со значением {v}")


if __name__ == '__main__':
    arithmetic(a=5, b=10, c=4, d=1)