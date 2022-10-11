#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This class that defines a square

        Args:
           size (int): the size of a square

    """

    def __init__(self, size=0):
        """Instantation of a private attribute 'size'
        this is done by runnin some try and except blocks
        to confirm size is of type 'int'

        Args:
           size (int): the size of a square

        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
