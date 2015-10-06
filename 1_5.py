import unittest

import lib
import math

class LibTest(unittest.TestCase):
    def test_def_sin(self):
        self.assertEqual(lib.sin(math.pi),0)
        self.assertEqual(lib.sin((math.pi)/6),0.5)
        self.assertEqual(lib.sin(3/2*math.pi),-1)
unittest.main(verbosity=2)
