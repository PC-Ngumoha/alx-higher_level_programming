#!/usr/bin/python3
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
  
    def setUp(self):
        self.rect = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        self.rect.width = 10
        self.rect.height = 2
        self.rect.x = 0
        self.rect.y = 0
        self.rect.id = 12

    def test_instance_ids(self):
        self.assertEqual(self.rect.id, 12)

    def test_instance_attribute_width(self):
        self.assertEqual(self.rect.width, 10)
        self.rect.width = 12
        self.assertEqual(self.rect.width, 12)
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(ValueError, Rectangle, -10, 4)

    def test_instance_attribute_height(self):
        self.assertEqual(self.rect.height, 2)
        self.rect.height = 4
        self.assertEqual(self.rect.height, 4)
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, 10, -4)

    def test_instance_attribute_x(self):
        self.assertEqual(self.rect.x, 0)
        self.rect.x = 3
        self.assertEqual(self.rect.x, 3)
        self.assertRaises(TypeError, Rectangle, 10, 4, "1", 2)
        self.assertRaises(ValueError, Rectangle, 10, 4, -5, 3)

    def test_instance_attribute_y(self):
        self.assertEqual(self.rect.y, 0)
        self.rect.y = 4
        self.assertEqual(self.rect.y, 4)
        self.assertRaises(TypeError, Rectangle, 10, 4, 1, "2")
        self.assertRaises(ValueError, Rectangle, 10, 4, 5, -3)

    def test_area(self):
        self.rect = Rectangle(2, 3)
        value = self.rect.area()
        self.assertEqual(value, 6)

    def test_str(self):
        output = "[Rectangle] (12) 0/0 - 10/2"
        self.assertEqual(str(self.rect), output)

    def test_display(self):
        #Rectangle without x and y coordinates specified
        display_rect = Rectangle(2, 3, 0, 0)
        expected = "##\n##\n##\n"
        result = prints_expected(display_rect, expected)
        self.assertIs(result, True)

        #Rectangle with only x coordinate specified
        display_rect = Rectangle(2, 3, 2, 0)
        expected = "  ##\n  ##\n  ##\n"
        result = prints_expected(display_rect, expected)
        self.assertIs(result, True)

        #Rectangle with only y coordinate specified
        display_rect = Rectangle(2, 3, 0, 2)
        expected = "\n\n##\n##\n##\n"
        result = prints_expected(display_rect, expected)
        self.assertIs(result, True)

        #Rectangle with both x and y coordinates specified
        display_rect = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        result = prints_expected(display_rect, expected)
        self.assertIs(result, True)

# Helper function for test_display TestCase
def prints_expected(display_rect, test_value):
    output = io.StringIO()
    sys.stdout = output
    display_rect.display()
    sys.stdout = sys.__stdout__
    if output.getvalue() == test_value:
        return True
    else:
        return False
        

if __name__ == '__main__':
    unittest.main()
