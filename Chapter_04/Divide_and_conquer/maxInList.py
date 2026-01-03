#!/usr/bin/python3

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    return list[0] if list[0] > max(list[1:]) else max(list[1:])


print(max([10, 1, 2, 100, 4, -20]))
