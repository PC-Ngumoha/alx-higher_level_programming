#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_instance_id_values(self):
        self.b1 = Base()
        self.b2 = Base(None)
        self.b3 = Base()
        self.b4 = Base(12)
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)


if __name__ == '__main__':
    unittest.main()
