#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mean(*arg):
    if 0 in arg:
        return "Имеется нуль"
    if arg:
        n = len(arg)
        h = 0.0
        for i in arg:
            h += 1/i
        h = n / h
        return h

    else:
        return None


if __name__ == '__main__':
    print("Введите числа через пробел: ")
    array = list(map(float, input().split()))
    print("Среднее гармоническое элементов: ", mean(*array))