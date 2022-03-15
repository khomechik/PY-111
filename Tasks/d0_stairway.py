from typing import Union, Sequence
from itertools import islice


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return -1
    if len(stairway) == 1:
        return stairway[0]

    before_last_price, last_price = stairway[0], stairway[1]
    for current_price in islice(stairway, 2, len(stairway)):
        before_last_price, last_price = last_price, min(before_last_price, last_price) + current_price

    return last_price
