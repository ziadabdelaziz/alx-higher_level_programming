#!/usr/bin/python3
"""
This module containes 'Node' class
for a Singly linked list
"""


class Node:
    """
    Node class for Singly Linked List
    """

    def __init__(self, data, next_node=None):
        """
        instantiate node with
        'data' and 'next_node' properties
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data setter
        make sure data is an integer
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        next node getter
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next node setter
        make sure the next node is None or Node
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        """
        Instantiate Singly linked list
        with head equals 'None'
        """
        self.__head = None

    def __str__(self):
        """
        Print the entire linked list
        """
        cur = self.__head
        singly_linked_list = ''
        print(cur)
        while (cur):
            singly_linked_list += str(cur.data)
            cur = cur.next_node
            if cur is not None:
                singly_linked_list += '\n'

        return singly_linked_list

    def sorted_insert(self, value):
        """
        Insert new node with increasing order
        """
        cur = self.__head
        prev = None
        new = Node(value)
        if cur is None:
            self.__head = new
            return

        if value <= cur.data:
            self.__head = new
            new.next_node = cur
            return

        while (cur):
            if cur.data >= value:
                prev.next_node = new
                new.next_node = cur
                return
            prev = cur
            cur = cur.next_node

        prev.next_node = new
