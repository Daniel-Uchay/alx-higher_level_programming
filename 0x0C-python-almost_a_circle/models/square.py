#!/usr/bin/python3
"""
    square.py module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Inicialitation method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>"""
        idd = self.id
        x = super().x
        y = super().y
        w = super().width
        return "[Square] ({}) {}/{} - {}".format(idd, x, y, w)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        idd = self.id
        x = super().x
        y = super().y
        w = super().width
        return {'x': x, 'y': y, 'id': idd, 'size': w}

    @property
    def size(self):
        """size getter"""
        return super().width

    @size.setter
    def size(self, size):
        """size setter"""
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the class"""
        if len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    super(Square, type(self)).width.fset(self, arg)
                    super(Square, type(self)).height.fset(self, arg)
                elif num == 2:
                    super(Square, type(self)).x.fset(self, arg)
                elif num == 3:
                    super(Square, type(self)).y.fset(self, arg)
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                super(Square, type(self)).width.fset(self, kwargs["size"])
                super(Square, type(self)).height.fset(self, kwargs["size"])
            if "x" in kwargs:
                super(Square, type(self)).x.fset(self, kwargs["x"])
            if "y" in kwargs:
                super(Square, type(self)).y.fset(self, kwargs["y"])
