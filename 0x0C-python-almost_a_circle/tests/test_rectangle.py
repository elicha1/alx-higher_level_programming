#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_area(self):
        # Test the area calculation
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_perimeter(self):
        # Test the perimeter calculation
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.perimeter(), 30)

    def test_initialization(self):
        # Test the initialization of the Rectangle instance
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
