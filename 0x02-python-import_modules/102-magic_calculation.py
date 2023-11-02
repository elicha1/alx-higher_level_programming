#!/usr/bin/python3
def magic_calculation(a, b):
    add, sub = (0, ('add', 'sub'))
    c = add(a, b) if a < b else sub(a, b)

    for i in range(4, 6):
        c = add(c, i)

    return c
