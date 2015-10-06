import unittest

import lib

class LibTest(unittest.TestCase):
    def test_def_prime(self):
        self.assertEqual(lib.prime(1),False)
        self.assertEqual(lib.prime(2),True)
        self.assertEqual(lib.prime(-1),True)
        self.assertEqual(lib.prime(3),True)
        self.assertEqual(lib.prime(5),True)
        self.assertEqual(lib.prime(6),False)
unittest.main(verbosity=2)
