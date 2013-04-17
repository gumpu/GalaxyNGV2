# vi: spell spl=en

class Universe(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__(self, size=400 ):
        self.size    = size
        self.planets = {}

    """Create a new universe populated with planets
    and nations.
    """
    def create(self):
        for i in xrange(0,200) :
            name = "%d" % i
            a_planet = Planet( name=name )
            self.place_planet( a_planet )
            key = a_planet.key()
            self.planets[ key ] = a_planet


    """Places a planet in a unique location
    """
    def place_planet( a_planet ):
        pass


    def distance(self, planet1, planet2):
        return 0


