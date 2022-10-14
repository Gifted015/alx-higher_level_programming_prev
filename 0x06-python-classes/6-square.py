#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This class that defines a square

        Args:
           size (int): the size of a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantation of a private attribute 'size'
        this is done by runnin some try and except blocks
        to confirm size is of type 'int'

        Args:
           size (int): the size of a square
           position (tuple): the space to be left before
                             printing size in my_print()

        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) != tuple or type(position[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(position) != 2 or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returns the current square area"""

        return (self.__size) ** 2

    @property
    def size(self):
        """Retrieve the value of __size"""

        return self.__size

    @size.setter
    def size(self, value=None):
        """Sets the value of __size"""

        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if (self.__size == 0):
            print("")
        else:
            rang = self.__size
            horiz = self.position[0]
            vert = self.position[1]
            for y in range(vert + rang):
                if (y < vert):
                    print("")
                    continue
                for x in range(horiz + rang):
                    if (x < horiz):
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(position) != tuple or type(position[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(position) != 2 or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
