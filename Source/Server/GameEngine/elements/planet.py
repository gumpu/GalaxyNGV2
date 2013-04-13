# vi: spell spl=en

class Planet(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = None

    """Compute the distance between this planet and
    another planet.
    """
    def dist( self, another_planet ):
        return 0

