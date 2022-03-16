from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        mid = len(container) // 2
        left = container[:mid]
        right = container[mid:]

        sort(left)
        sort(right)

        # Two counters for running through two halves
        i = 0
        j = 0

        # counter for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                container[k] = left[i]
                i += 1
            else:
                container[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            container[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            container[k] = right[j]
            j += 1
            k += 1

    return container
