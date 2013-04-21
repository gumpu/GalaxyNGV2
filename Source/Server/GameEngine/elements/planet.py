# vi: spell spl=en

class Planet(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.name = name
        self.size = 0
        self.population = 0
        self.colonists  = 0
        self.resources  = 0

    """Compute the distance between this planet and
    another planet.
    """
    def dist( self, another_planet ):
        return 0


    def key( self ):
        k = "%d,%d" % (self.x, self.y)
        return k

    def report( self ):
        print ( "%s %d %d" % (self.name, self.x, self.y) )

