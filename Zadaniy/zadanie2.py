#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее гармоническое
своих аргументов a1, a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


def harmonic_mean(*arg):
    x = 0
    if arg:
        for i in arg:
            if i == 0:
                return None
            else:
                x += 1 / float(i)
        harmonic = 1 / (1 / len(arg) * x)
        return harmonic
    else:
        return None


if __name__ == '__main__':
    print('Введите список аргументов: ')
    array = list(map(float, input().split()))
    print(harmonic_mean(*array))