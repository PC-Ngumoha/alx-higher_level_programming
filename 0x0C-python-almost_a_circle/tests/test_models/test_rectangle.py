#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
   
    def test_instance_ids(self):
        self.rect1 = Rectangle(10, 2, 0, 0, 1)
        self.rect2 = Rectangle(10, 3, 0, 0, 12)
        self.rect3 = Rectangle(1, 4, 1, 3, 2)
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect2.id, 12)
        self.assertEqual(self.rect3.id, 2)

    def test_instance_width(self):
        self.rect1 = Rectangle(10, 2)
        self.assertEqual(self.rect1.width, 10)
        self.rect1.width = 12
        self.assertEqual(self.rect1.width, 12)
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(ValueError, Rectangle, -10, 4)

    def test_instance_height(self):
        self.rect1 = Rectangle(10, 2)
        self.assertEqual(self.rect1.height, 2)
        self.rect1.height = 4
        self.assertEqual(self.rect1.height, 4)
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, 10, -4)

    def test_instance_x(self):
        self.rect3 = Rectangle(1, 4, 1, 3)
        self.assertEqual(self.rect3.x, 1)
        self.rect3.x = 3
        self.assertEqual(self.rect3.x, 3)
        self.assertRaises(TypeError, Rectangle, 10, 4, "1", 2)
        self.assertRaises(ValueError, Rectangle, 10, 4, -5, 3)

    def test_instance_y(self):
        self.rect3 = Rectangle(1, 4, 1, 3)
        self.assertEqual(self.rect3.y, 3)
        self.rect3.y = 4
        self.assertEqual(self.rect3.y, 4)
        self.assertRaises(TypeError, Rectangle, 10, 4, 1, "2")
        self.assertRaises(ValueError, Rectangle, 10, 4, 5, -3)


if __name__ == '__main__':
    unittest.main()
