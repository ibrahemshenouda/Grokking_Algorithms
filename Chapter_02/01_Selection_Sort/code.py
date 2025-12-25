#!/usr/bin/python3

# Time Complexity:  O(n*n)
# Algorithm Idea: find smallest or greatest every step

def find_smallest(arr):
    # suppose smallest is the first element
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    # to store smallest every iteration
    new_arr = []

    # to pop smallest after find by index returned from find_smallest()
    copied_arr = list(arr)

    for i in range(len(copied_arr)):
        # find_smallest index by find_smallest()
        smallest = find_smallest(copied_arr)
        # remove smallest from copied_arr, adding smallest to new_arr
        new_arr.append(copied_arr.pop(smallest))

    return new_arr


print(selection_sort([3, 2, 4, 1, 7, 3, 5, 8]))
