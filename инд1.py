##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = 1
    for i in A:
        if i % 3 == 0:
            if i > 0:
                s *= i
    print(s)
