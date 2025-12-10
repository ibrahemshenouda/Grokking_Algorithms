#!/usr/bin/python3

def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if item == guess:
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid+1
    return None


my_list = [1, 2, 3, 4, 5, 6]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
