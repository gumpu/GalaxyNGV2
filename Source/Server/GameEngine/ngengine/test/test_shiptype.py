#!/usr/bin/env python

import unittest
from ngengine.elements.shiptype import Shiptype


class ShiptypeTestCase(unittest.TestCase):

    def setUp(self):
        self.drone     = Shiptype(0,'drone', 1, 0, 0, 0,0)
        self.flak      = Shiptype(0,'flak', 1, 0, 0, 2, 0)
        self.destroyer = Shiptype(0,'destroyer', 6, 3, 4, 4, 0)
        self.freighter = Shiptype(0,'freighter', 30.00, 0, 0.00, 9.50, 10.00)

    def test_mass(self):
        self.assertAlmostEqual(self.drone.mass(), 1.0)
        self.assertAlmostEqual(self.flak.mass(), 3.0)
        self.assertAlmostEqual(self.destroyer.mass(), 18.0)
        self.assertAlmostEqual(self.freighter.mass(), 49.50)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShiptypeTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

