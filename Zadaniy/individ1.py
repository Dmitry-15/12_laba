#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите функцию, принимающую произвольное количество аргументов,
и возвращающую произведение аргументов, расположенных после
максимального по мо дулю аргумента.
Если функции передается пустой список аргументов,
то она должна возвращать значение  None.
В процессе решения не использовать преобразования конструкции  *args
в список или иную структуру данных
"""


def min_max(*args):

    # Результат
    if len(args) == 0:
        return None
    composition = 1

    # Индекс и item для максимального
    max_arg = args[0]
    max_ind = 0

    # Ищет максимальный аргумет
    for i, item in enumerate(args):
        if item > max_arg:
            max_arg = item
            max_ind = i

    # После максимального элемента умножает все элементы
    for i in args[max_ind + 1:]:
        composition *= i
    return composition


if __name__ == '__main__':
    arg = list(map(float, input('Введите список аргументов: ').split()))
    print(min_max(*arg))