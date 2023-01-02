#!/usr/bin/python3
""" This module contain a class defining a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initialize width and height fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Public method that returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Public method that returns a printable rectangle"""
        rect = ""
        if self.height != 0 and self.width != 0:
            for i in range(self.height):
                for j in range(self.width):
                    rect += "{}".format("#")
                if i < self.height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """Public method returns a string representation of a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Public method that delete instance and print message"""
        print("Bye rectangle...")
