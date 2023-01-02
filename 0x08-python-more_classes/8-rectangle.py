#!/usr/bin/python3
""" This module contain a class defining a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that initialize width and height fields"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    rect += "{}".format(self.print_symbol)
                if i < self.height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """Public method returns a string representation of a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Public method that delete instance and print message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method returns the biggest rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height
        if area1 > area2:
            return rect_1
        elif area2 > area1:
            return rect_2
        return rect_1
