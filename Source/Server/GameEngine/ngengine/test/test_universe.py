#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from ngengine.game import Game
from ngengine.universe import Universe, distance, PlanetPlacementError
from ngengine.elements.planet import Planet

class UniverseTestCase(unittest.TestCase):

    def test_place_planet( self ):
        """Trying adding 40 planets in a large universe"""
        universe = Universe()
        universe.size = 500
        for n in range(0, 40):
            a_planet = Planet(name='test')
            universe.place_planet(a_planet)
            universe.add_planet(a_planet)
        self.assertEqual(len( universe.planets ), 40 )


    def test_place_planet_exception( self ):
        """Trying to add to many planets should fail"""
        universe = Universe()
        universe.size = 5  # So no more than 36 planets can fit
        with self.assertRaises(PlanetPlacementError):
            # This should raise an exception
            for n in range(0, 40):
                a_planet = Planet(name='test')
                universe.place_planet(a_planet)
                universe.add_planet(a_planet)

    def test_distance( self ):
        """Computing distances between planets"""
        p1 = Planet('1')
        p2 = Planet('2')
        self.assertEqual(distance( p1, p2 ), 0)
        p1.x = 40
        self.assertEqual(distance( p1, p2 ), 40)
        p2.x = 40
        self.assertEqual(distance( p1, p2 ), 0)
        p2.y = 80
        self.assertEqual(distance( p1, p2 ), 80)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UniverseTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

