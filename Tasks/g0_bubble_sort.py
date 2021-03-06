from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(len(container)):
        for j in range(len(container) - 1 - i):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]

    return container
