#!/usr/bin/python3

def sum(arr):
    # Base case
    if len(arr) == 0:
        return 0

    current_num = arr[0]
    arr.pop(0)

    return current_num + sum(arr)


print(sum([10, 20, 30, 40]))
