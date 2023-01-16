#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
import sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareclass(unittest.TestCase):
    """Test Cases Class"""
    def setUp(self):
        """Set up"""
        self.inst = Square(2, 3, 4, 5)

    def tearDown(self):
        """ Tear Dowm"""
        del self.inst
        Base._Base__nb_objects = 0

    def test_to_dict(self):
        """ Tear Dowm"""
        r1 = self.inst.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(r1, exp)

    def test_to_dict_1(self):
        """ Tear Dowm"""
        r1 = self.inst.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(type(r1).__name__, type(exp).__name__)

    def test_area(self):
        """ Test Area"""
        self.assertEqual(self.inst.area(), 4)

    def test_get_set_size(self):
        """ Test Area"""
        self.inst.size = 30
        self.assertEqual(str(self.inst), "[Square] (5) 3/4 - 30")

    def test_get_set_size_e(self):
        """ Test Area"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.size = "Fault"

    def out_c(self, x=None):
        """ Out std"""
        t = sys.stdout
        sys.stdout = StringIO()
        if x is None:
            self.inst.display()
        else:
            x.display()
        o = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = t
        return o

    def test_display(self):
        """ Test display"""
        display = "\n\n\n\n   ##\n   ##\n"
        o = self.out_c()
        self.assertEqual(o, display)

    def test_display_1(self):
        """ Test display"""
        r1 = Rectangle(4, 6)
        display = "####\n####\n####\n####\n####\n####\n"
        o = self.out_c(r1)
        self.assertEqual(o, display)

    def test_str(self):
        """ Test display"""
        self.assertEqual(str(self.inst), "[Square] (5) 3/4 - 2")

    def test_update_att(self):
        """ Test display"""
        self.inst.update(89)
        self.assertEqual(str(self.inst), "[Square] (89) 3/4 - 2")

    def test_update_dic(self):
        self.inst.update(x=6, y=3, size=7)
        self.assertEqual(str(self.inst), "[Square] (5) 6/3 - 7")

    def test_id(self):
        """ Test id"""
        self.assertEqual(self.inst.id, 5)

    def test_id_1(self):
        """ Test id 1"""
        self.inst.id = 0
        inst1 = Rectangle(1, 2)
        inst2 = Rectangle(2, 1)
        inst3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(inst3.id, 3)

    def test_width(self):
        """ test width"""
        self.assertEqual(self.inst.width, 2)

    def test_height(self):
        """ test height"""
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """ test x"""
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """ test y"""
        self.assertEqual(self.inst.y, 4)

    def test_raise_width(self):
        """ test raise width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.width = "Fault"

    def test_raise_height(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.inst.height = "Fault"

    def test_raise_x(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.inst.x = "Fault"

    def test_raise_y(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.inst.y = "Fault"

    def test_raise_width_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.inst.width = 0

    def test_raise_height_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.inst.height = 0

    def test_raise_x_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.inst.x = -1

    def test_raise_y_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.inst.y = -1
