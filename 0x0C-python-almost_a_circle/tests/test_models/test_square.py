import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):       
        self.sqr = Square(10, 0, 0, 1)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.sqr.width, 10)
        self.assertEqual(self.sqr.height, 10)
        self.assertEqual(self.sqr.x, 0)
        self.assertEqual(self.sqr.y, 0)
        self.assertEqual(self.sqr.id, 1)

    def test_str(self):
        expected = "[Square] (1) 0/0 - 10"
        self.assertEqual(str(self.sqr), expected)
