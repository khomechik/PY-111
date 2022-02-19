"""
Priority Queue

Queue priorities are from 0 to 10
"""

from typing import Any


class PriorityQueue:
    def __init__(self, priorities=11):
        self._priorities = priorities

        self._priority_queue = {priority: [] for priority in range(priorities)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing

        """
        if priority in range(self._priorities):
            self._priority_queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        for priority in range(self._priorities):
            if self._priority_queue[priority]:
                return self._priority_queue[priority].pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if priority in range(self._priorities):
            if ind < len(self._priority_queue[priority]):
                return self._priority_queue[priority][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        for priority in range(self._priorities):
            if self._priority_queue[priority]:
                self._priority_queue[priority].clear()