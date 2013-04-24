# vi: spell spl=en

from elements.turn import Turn
from elements.ukey import UKey

class Game(object):

    """Game -- all data for a single game.
    """
    def __init__(self):
        self.name = None
        self.turn = []
        self.ukey = UKey() # Unique key generator

    def create(self, game_options):
        """Create a new game
        """
        # Create turn 0
        self.turn.append(Turn())
        self.turn[0].create(game_options, self.ukey)

    def run(self, orders_set):
        """Given a set with orders for one or more nations compute the next
        turn in the game,
        """
        pass

    def report(self):
        """Create the turn reports.
        """
        pass

    def statistics(self):
        pass

