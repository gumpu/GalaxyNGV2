# vi: spell spl=en

from elements.universe import Universe

class Turn(object):
    """Data for a single turn
    """

    def __init__(self):
        self.universe = None
        self.nations  = {}
        self.number   = 0

    def create( self, game_options ):
        self.universe = Universe()
        self.universe.create()


