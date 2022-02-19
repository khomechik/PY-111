"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if not arr:
        return -1
    else:
        min_index = 0
        for current_index, current_item in enumerate(arr):
            if current_item < arr[min_index]:
                min_index = current_index
        return min_index


