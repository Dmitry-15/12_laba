#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Найти среднеквадратическое отклонение и минимальное
значение в списке именованных аргументов.
"""


def disp(**kwargs):
    n = len(kwargs.values())
    s = sum(kwargs.values())
    sigma = 0
    min_val = min(kwargs.values())
    for k, v in kwargs.items():
        if v == min_val:
            print(f"Наименьшая переменная {k} со значением {v}")
    for a in kwargs.values():
        sigma += (a - s) ** 2
    dev = (sigma / (n - 1)) ** 0.5
    print(f"Среднеквадратическое отклонение - {dev}")


if __name__ == '__main__':
    disp(a=1, b=2, c=3, d=6, e=4, f=2)