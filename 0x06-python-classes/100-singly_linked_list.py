#!/usr/bin/python3
# 100-singly_linked_list.py
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list.

    Attributes:
        data (int): The data of the node.
        next_node (Node): The next node in the list.

    Methods:
        __init__(self, data, next_node=None): Initialize a new Node.

    Properties:
        data: Get/set the data of the Node.
        next_node: Get/set the next_node of the Node.

    Raises:
        TypeError: If data is not an integer or if next_node is not a Node
        object or None.

    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.

        Raises:
            TypeError: If data is not an integer or if next_node is not a Node
            object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node.

        Args:
            value (Node): The new next_node value.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list.

    Methods:
        __init__(self): Initialize a new SinglyLinkedList.
        sorted_insert(self, value): Insert a new Node to the SinglyLinkedList.

    Attributes:
        __head (Node): The head of the singly-linked list.

    """

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)
