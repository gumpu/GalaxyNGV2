# vi: spell spl=en

from elements.turn import Turn
from elements.ukey import UKey
from reports.turn_report import TurnReport

class Game(object):

    """Game -- all data for a single game.
    """
    def __init__(self):
        self.name = None
        self.turn = []
        self.ukey = UKey() # Unique key generator

    def create( self, game_options ):
        """Create a new game
        """
        # Create turn 0
        self.turn.append(Turn())
        self.turn[0].create(game_options, self.ukey)

    def run( self, orders_set ):
        """Given a set with orders for one or more nations compute the next
        turn in the game,
        """
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


