#!/usr/bin/python3
"""Class ``Node`` and ``SinglyLinkedList`` are defined in this module.
"""

class Node:
    """Class ``Node`` definition.
    """
    def __init__(self, data, next_node=None):
        """Initialize the Node object.
        Args:
            data (int): The data section of the Node.
            next_node (Node): A pointer to the next node on the list.
        Raises:
            TypeError: If any of the values supplied is of the wrong type.
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError('data must be an integer')
        if isinstance(next_node, Node) or next_node == None:
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """data property.
        @data.setter
        Args:
            data (int): integer data to be saved on a Node on the list
        Raises:
            TyperError: If any of the values supplied is of the wrong type.
        """
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """next node on the linked-list.
        @next_node.setter
        Args:
            next_node (Node): next node on the linked list
        Raises:
            TypeError: If any of the values supplied is of the wrong type.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if isinstance(next_node, Node) or next_node == None:
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    """Class ``SinglyLinkedList`` definition.
    """
    def __init__(self):
        """Initialize the singly linked list.
        """
        self.__head = None

    def __str__(self):
        """String representation of the Linked list.
        """
        temp = self.__head
        while temp != None:
            print(temp.data)
            temp = temp.next_node

    def sorted_insert(self, value):
        """Inserts a new Node into a sorted Linked list.
        Args:
            value (int): integer data in the new Node.
        """
        new_node = Node(value)
        curr = self.__head
        if curr == None:
            curr = new_node
        else:
            while (curr.next_node).data < new_node.data \
                and curr.next_node != None:
                curr = curr.next_node
            if (curr.next_node).data >= new_node.data:
                new_node.next_node = curr.next_node
                curr.next_node = new_node
            else:
                curr.next_node = new_node

