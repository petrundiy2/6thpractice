import unittest

import lib

class LibTest(unittest.TestCase):
    def test_def_palindrome(self):
        self.assertEqual(lib.palindrome('1221'),True)
        self.assertEqual(lib.palindrome('4'),False)
        self.assertEqual(lib.palindrome('12321'),True)
unittest.main(verbosity=2)
