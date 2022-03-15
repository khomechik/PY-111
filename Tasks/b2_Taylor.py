from typing import Union

import math

from itertools import count


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    epsilon = 0.0001
    sum_x = 0
    s = 1
    i = 1
    while s > epsilon:
        sum_x += s
        s = (x ** i) / math.factorial(i)
        i += 1
    return sum_x


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    epsilon = 0.0001
    sum_sin = 0
    for i in count(1, 1):
        current_item = ((-1) ** (i - 1) * x ** (2 * i - 1)) / math.factorial(2 * i - 1)
        sum_sin += current_item
        if abs(current_item) <= epsilon:
            return sum_sin

