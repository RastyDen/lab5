#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) произведение отрицательных элементов списка;
# 2) сумму положительных элементов списка, расположенных до максимального элемента.
# Изменить порядок следования элементов в списке на обратный.

import sys
import math

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input('Введите элементы: ').split()))

    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Произведение отрицательных элементов списка
    c = 1
    for i in a:
        if i < 0:
            c *= i

    # Сумма положительных элементов списка, расположенных до максимального элемента.
    b = sum([i for i in a[0:-1] if i > 0])

    # Вывод результатов.
    print(f'Произведение отрицательных элементов списка = {c}\n'
          f'Сумма положительных элементов списка, расположенных до максимального элемента. {b}\n'
          f'Измененный порядок следования элементов в списке на обратный {a[::-1]}.')
