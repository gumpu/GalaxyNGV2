# vi: spell spl=en

from elements.planet import Planet
from random import randint
import math


def planet_namer():
    """Generator for the initial names of the planets"""
    n = 0
    while True:
        n = n + 1
        yield( str(n) )

def distance( planet1, planet2 ):
    """Distance between two planets in the universe"""
    dx = planet1.x - planet2.x
    dy = planet1.y - planet2.y
    return math.sqrt( dx*dx + dy*dy )


class PlanetPlacementError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Universe(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__( self, size=400 ):
        self.owner   = None
        self.size    = size
        self.planets = {}


    def create( self, options, nations ):
        """Create a new universe populated with planets and nations.
        """
        pn = planet_namer()
        self.size = options.universe_size

        for owner in nations.itervalues():
            a_planet = Planet( name=pn.next() )

            for n in xrange( 0, 100 ):
                self.place_planet( a_planet )
                far_enough = True
                for other_planet in self.planets.itervalues():
                    if distance( other_planet, a_planet ) < options.min_distance :
                        far_enough = False
                if far_enough :
                    break;

            if not far_enough :
                raise PlanetPlacementError(
                        "Cannot place home planet far enough from other home planets." )
            key = a_planet.key()
            a_planet.owner = owner.key
            # Make it official
            self.add_planet(  a_planet )

    def add_planet( self, a_planet ):
        key = a_planet.key()
        self.planets[key] = a_planet

    def place_planet( self, a_planet ):
        """Places a planet in a unique location
        """
        a_planet.x = randint( 0, self.size )
        a_planet.y = randint( 0, self.size )
        # TODO: Make sure two planets
        # do not occupy the same location

    def report( self ):
        for (key,p) in iter(sorted(self.planets.items())) :
            p.report()

    def map( self, map_file ):
        map_file.write( "x,y,name\n" )
        for p in self.planets.itervalues() :
            map_file.write( "%d,%d,%s\n" % (p.x, p.y, p.name) )

