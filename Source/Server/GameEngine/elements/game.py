# vi: spell spl=en

from elements.turn import Turn
from elements.ukey import UKey

class Game(object):

    """Game -- all data for a single game.
    """
    def __init__(self):
        self.name = None
        self.turn = []
        self.ukey = UKey()

    """Create a new game
    """
    def create(self, game_options):
        # Create turn 0
        self.turn.append(Turn())
        self.turn[0].create(game_options)


