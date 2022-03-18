"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, key: int, value: Any):
        self.key: int = key
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    @staticmethod
    def is_valid_node(value):
        if not isinstance(value, (Node, type(None))):
            raise ValueError
        return True

    @property
    def left(self) -> Optional["Node"]:
        return self._left

    @left.setter
    def left(self, value):
        if self.is_valid_node(value):
            self._left = value

    @property
    def right(self) -> Optional["Node"]:
        return self._right

    @right.setter
    def right(self, value):
        if self.is_valid_node(value):
            self._right = value

    def __eq__(self, other):
        if isinstance(other, int):
            return self.key == other
        elif isinstance(other, Node):
            return self.key == other.key

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.key < other
        elif isinstance(other, Node):
            return self.key < other.key

        return NotImplemented

    def __str__(self):
        return f"<{self.key}>"

    def is_list(self) -> bool:
        return self.left is self.right is None


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """

        current_node, prev_node = self._find(key)
        if current_node is not None:
            current_node.value = value
            return

        new_node = Node(key, value)
        if prev_node is None:
            self._root = new_node

        elif new_node < prev_node:
            prev_node.left = new_node
        else:
            prev_node.right = new_node

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        current_node, prev_node = self._find(key)
        if current_node is None:
            return

        if current_node.is_list():
            current_node = None

        else:
            if current_node.right is None:
                current_node.value = current_node.left

            elif current_node.left is None:
                current_node.value = current_node.right

            else:
                min_node = current_node.right
                while min_node.left:
                    min_node = min_node.left
                return min_node
                current_node.value = min_node
                min_node = None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """

        current_node, _ = self._find(key)
        if current_node is not None:
            return current_node.value
        else:
            raise KeyError

    def _find(self, key) -> Tuple[Optional[Node], Optional[Node]]:
        current_node, prev_node = self._root, None
        while current_node is not None:
            if current_node == key:
                break

            prev_node = current_node
            if current_node < key:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return current_node, prev_node

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self._root = None
