# -*- coding:utf-8 -*-
"""This module is used to implement binary search algorithm """


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = list[middle]
        if guess == item:
            return middle
        elif guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, 10))
