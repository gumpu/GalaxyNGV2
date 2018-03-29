from ngengine.elements import planet

import random
class UKey(object):
    """Unique key generator.
    Used to give all elements in the game a unique id.
    This makes it easier to compute what happened after
    name changes by the players.

    Could have used uuid here, but that would have been
    overkill.
    """
    def __init__(self):
        self.unique_key = 1

    def next(self):
        """Get the next unique key
        """

        # Adding the random element makes it slightly more difficult
        # for a player to gain information about other players
        # from the unique keys.
        self.unique_key = self.unique_key + random.randint(1,5)
        return self.unique_key


class Game():

    """Game -- all data for a single game.
    """
    def __init__(self):
        self.name = None
        self.turn = []
        # self.ukey = UKey() # Unique key generator

    def create(self, game_options):
        """Create a new game
        """
        pass

    def run(self, orders_set):
        pass

    def report( self ):
        """Create the turn reports for each nation in the game.

        Returns an array of turn reports.
        """
        turn_reports = []
        for a_nation in self.turn[-1].nations.itervalues():
            a_report = TurnReport( a_nation, len( self.turn ) - 1 )
            a_report.gather( self.turn[-1] )
            turn_reports.append( a_report )
        return turn_reports

    def statistics( self ):
        pass

    def map( self, file ):
        """Create a map of the universe"""

        # Always make the map for the latest turn.
        self.turn[-1].map( file )

