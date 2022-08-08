#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    def test_instance_id_values(self):
        b1 = Base()
        b2 = Base(None)
        b4 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 12)

    def test_to_json_string(self):
        rect = Rectangle(2, 3, 0, 0, 1)
        rect_dict = rect.to_dictionary()
        expected = '[{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([rect_dict]), expected)

        sqr = Square(2, 0, 0, 1)
        sqr_dict = sqr.to_dictionary()
        expected = '[{"id": 1, "size": 2, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([sqr_dict]), expected)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]'
        expected = [{'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0}]
        self.assertListEqual(Base.from_json_string(json_string), expected)



if __name__ == '__main__':
    unittest.main()
