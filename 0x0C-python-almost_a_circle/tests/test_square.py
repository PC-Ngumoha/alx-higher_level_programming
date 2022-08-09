import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):       
        self.sqr = Square(10, 0, 0, 1)

    def tearDown(self):
        self.sqr.size = 10
        self.sqr.x = 0
        self.sqr.y = 0
        self.sqr.id = 1

    def test_init(self):
        self.assertEqual(self.sqr.width, 10)
        self.assertEqual(self.sqr.height, 10)
        self.assertEqual(self.sqr.x, 0)
        self.assertEqual(self.sqr.y, 0)
        self.assertEqual(self.sqr.id, 1)

    def test_str(self):
        expected = "[Square] (1) 0/0 - 10"
        self.assertEqual(str(self.sqr), expected)

    def test_size(self):
        self.sqr.size = 12
        
        self.assertEqual(self.sqr.width, 12)
        self.assertEqual(self.sqr.height, 12)
        
        with self.assertRaises(TypeError):
            self.sqr.size = "12"
        
        with self.assertRaises(ValueError):
            self.sqr.size = -12

    def test_update(self):
        self.sqr.update(12, 30, 1, 2)
        expected = "[Square] (12) 1/2 - 30"
        self.assertEqual(str(self.sqr), expected)

        self.sqr.update(x=2, y=1, id=13, size=31)
        expected = "[Square] (13) 2/1 - 31"
        self.assertEqual(str(self.sqr), expected)

    def test_to_dictionary(self):
        sqr_dictionary = self.sqr.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 0, 'y': 0}
        self.assertDictEqual(sqr_dictionary, expected)
