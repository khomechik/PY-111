from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    elements = len(container)

    if elements < 2:
        return container

    current_position = 0

    for i in range(1, elements):
        if container[i] <= container[0]:
            current_position += 1
            temp = container[i]
            container[i] = container[current_position]
            container[current_position] = temp

    temp = container[0]
    container[0] = container[current_position]
    container[current_position] = temp

    left = sort(container[0:current_position])
    right = sort(container[current_position + 1:elements])

    container = left + [container[current_position]] + right
    return container