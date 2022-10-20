#!/usr/bin/python3
"""This is a module for a defining a class named Rectangle"""


class Rectangle:
    """The class Rectangle
    Attributes:
       width (int) - a private attribute
                     which serves as the width of the rectangle
       height (int)- a private attribute
                     which serves as the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = height
        if (type(height) != int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__height == 0 or self.width == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ("")
        else:
            cont = ""
            for h in range(self.__height):
                for w in range(self.__width):
                    cont += str(self.print_symbol)
                if (h != self.__height - 1):
                    cont += "\n"
            return cont

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) != Rectangle):
            print(type(rect_1))
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) != Rectangle):
            print(type(rect_2))
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area()):
            return rect_1
        else:
            return rect_2
        
