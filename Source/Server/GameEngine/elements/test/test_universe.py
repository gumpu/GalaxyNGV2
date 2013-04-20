#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from elements.game import Game


class UniverseTestCase(unittest.TestCase):

    def test_dummy(self):
        pass


if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UniverseTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

