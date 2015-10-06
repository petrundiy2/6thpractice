import unittest

import lib

class LibTest(unittest.TestCase):
    def test_def_factorial(self):
        self.assertEqual(lib.factorial(-1),1)
        self.assertEqual(lib.factorial(4),24)
        self.assertEqual(lib.factorial(0),1)
unittest.main(verbosity=2)
