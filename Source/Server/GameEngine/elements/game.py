# vi: spell spl=en


from elements.planet import Planet
from elements.universe import Universe

class Game(object):

    """Game -- all data for a single game.
    """
    def __init__(self):
        self.universe = None
        self.nations  = {}


    """Create a new game
    """
    def create(self, game_options ):
        self.universe = Universe()
