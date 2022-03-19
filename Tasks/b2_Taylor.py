from typing import Union

import math


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    e_to_x = 0
    for i in range(10):
        e_to_x += x ** i / math.factorial(i)
    return e_to_x


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    sin_x = 0
    for i in range(1, 10):
        sin_x += ((-1) ** (i - 1) * x ** (2 * i - 1)) / math.factorial(2 * i - 1)

    return sin_x


