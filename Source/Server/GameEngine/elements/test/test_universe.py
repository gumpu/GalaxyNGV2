#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from elements.game import Game
from elements.universe import Universe, distance, PlanetPlacementError
from elements.planet   import Planet

class UniverseTestCase(unittest.TestCase):

    def test_place_planet( self ):
        universe = Universe()
        universe.size = 5  # So no more than 25 planets can fit
        for n in xrange( 0, 25 ):
            a_planet = Planet( name='test' )
            universe.place_planet( a_planet )
            universe.add_planet( a_planet )

        a_planet = Planet( name='test' )
        # This should raise an exception
        with self.assertRaises( PlanetPlacementError ):
            universe.place_planet( a_planet )

    def test_distance( self ):
        p1 = Planet( '1' )
        p2 = Planet( '2' )
        self.assertEqual( distance( p1, p2 ), 0 )
        p1.x = 40
        self.assertEqual( distance( p1, p2 ), 40 )
        p2.x = 40
        self.assertEqual( distance( p1, p2 ), 0 )
        p2.y = 80
        self.assertEqual( distance( p1, p2 ), 80 )

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UniverseTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

