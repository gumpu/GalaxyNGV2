#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from   ngengine.elements.planet import Planet, PROD_CAPITAL

class PlanetTestCase(unittest.TestCase):

    def test_population_growth(self):
        """TODO Population growth"""
        self.assertTrue(True) # TODO

    def test_is_occupied( self ):
        """Is planet occupied test"""
        p = Planet('Test')
        self.assertTrue( not p.is_occupied() )
        p.owner = 1
        self.assertTrue( p.is_occupied() )

    def test_capital_production(self):
        """Production of capital for various planet sizes"""
        p = Planet( 'Test' )
        p.population = 1000.0
        p.industry   = 1000.0
        p.resources  = 10.0
        p.product    = PROD_CAPITAL

        p.produce()
        self.assertAlmostEqual(p.capital, 196.08, delta=0.005)

        p2 = Planet('2')
        p2.population = 1000.0
        p2.industry   = 1000.0
        p2.resources  = 10.0
        p2.materials  = 200
        p2.product    = PROD_CAPITAL

        p2.produce()
        self.assertAlmostEqual(p2.capital, 200, delta=0.05)

        p3 = Planet('3')
        p3.population = 1000.0
        p3.industry   = 1000.0
        p3.resources  = 0.1
        p3.materials  = 0
        p3.product    = PROD_CAPITAL

        p3.produce()
        self.assertAlmostEqual(p3.capital, 66.67, delta=0.05)


if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PlanetTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

