# vi: spell spl=en

from elements.planet import Planet
from random import randint


class Universe(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__(self, size=400):
        self.owner   = None
        self.size    = size
        self.planets = {}

    def create(self, options):
        """Create a new universe populated with planets and nations.
        """
        self.size = options.universe_size
        for i in xrange(0,10) :
            name = "%d" % i
            a_planet = Planet(name=name)
            self.place_planet(a_planet)
            key = a_planet.key()
            self.planets[key] = a_planet
            # TODO: Make sure two planets
            # do not occupy the same location

    def place_planet(self, a_planet):
        """Places a planet in a unique location
        """
        a_planet.x = randint(0,self.size)
        a_planet.y = randint(0,self.size)

    def distance(self, planet1, planet2):
        return 0

    def report(self):
        for (key,p) in iter(sorted(self.planets.items())) :
            p.report()

