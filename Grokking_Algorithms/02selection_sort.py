# -*- coding:utf-8 -*-
"""This module is used to implement selection sort algorithm """


def find_small_element_index(arr):
    small_element = arr[0]
    small_element_index = 0
    for i in range(1, len(arr)):
        if arr[i] < small_element:
            small_element = arr[i]
            small_element_index = i
    return small_element_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        small_element_index = find_small_element_index(arr)
        new_arr.append(arr.pop(small_element_index))
    # 列表生成式，更加简洁
    # new_arr = [arr.pop(find_small_element_index(arr)) for i in range(len(arr))]
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
