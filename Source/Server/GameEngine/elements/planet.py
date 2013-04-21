# vi: spell spl=en


PROD_CAPITAL  = 1
PROD_SHIP     = 2
PROD_MATERIAL = 3

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
        self.material   = 0
        self.capital    = 0
        self.production = None

    """Compute the distance between this planet and
    another planet.
    """
    def dist(self, another_planet):
        return 0


    """Gives a unique key that says the same during
    the whole game.
    """
    def key(self):
        k = "%d,%d" % (self.x, self.y)
        return k

    def report(self):
        print ( "%s %d %d" % (self.name, self.x, self.y) )


    def produce(self):
        if self.production   == PROD_MATERIAL:
            pass
        elif self.production == PROD_SHIP:
            pass
        elif self.production == PROD_MATERIAL:
            pass
        else
            pass

