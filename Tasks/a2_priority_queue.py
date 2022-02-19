"""
Priority Queue

Queue priorities are from 0 to 10
"""

from typing import Any


class PriorityQueue:
    def __init__(self):

        self._priority_queue = {queue: [] for queue in range(11)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing

        """
        if priority in self._priority_queue.keys():
            self._priority_queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        for queue_index in range(11):
            if self._priority_queue[queue_index]:
                return self._priority_queue[queue_index].pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if priority in self._priority_queue.keys():
            if ind < len(self._priority_queue[priority]):
                return self._priority_queue[priority][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        for queue_index in range(11):
            if self._priority_queue[queue_index]:
                self._priority_queue[queue_index].clear()


