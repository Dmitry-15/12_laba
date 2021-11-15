#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее геометрическое
своих аргументов a1, a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


def mean(*arg):
    if arg:
        a = 1.0
        for i in arg:
            a *= i
        a = a ** (1 / len(arg))
        return a
    else:
        return None


if __name__ == '__main__':
    print('Введите список аргументов: ')
    array = list(map(float, input().split()))
    print(mean(*array))
