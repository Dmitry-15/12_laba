#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mean(*arg):
    if arg:
        a = 1.0
        k = 1

        for i in arg:
            a *= i * k
        a = a ** (1/len(arg))
        return a

    else:
        return None


if __name__ == '__main__':
    print("Введите числа через пробел: ")
    array = list(map(float, input().split()))
    print("Среднее геометрическое элементов: ", mean(*array))
