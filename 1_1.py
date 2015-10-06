import unittest

import lib

class LibTest(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(lib.even(2),True)
        self.assertEqual(lib.even(-4),True)
    def test_not_even_numbers(self):
        self.assertEqual(lib.even(9),False)
        self.assertEqual(lib.even(-7),False)
unittest.main(verbosity=2)
