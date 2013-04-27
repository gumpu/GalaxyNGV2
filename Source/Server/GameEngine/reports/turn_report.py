# vi: spell spl=en

from reports.planet_report import PlanetReport

class TurnReport(object):

    """A collection of information about the current state of
    the turn from the perspective of a nations.

    Is a subset of all information on the planets, groups,
    nations etc, but with some parts removed or partially removed
    because they were not visible to the nation.

    Information is this report is send to the client.
    """
    def __init__( self, nation, turn_number ):
        self.nation = nation
        self.turn_number = turn_number
        self.planets = []
        # self.battles
        # self.nations
        # self.messages

    def gather( self, a_turn ):
        """Gather all information for the perspective of the
        nation for which this report is.
        """
        for a_planet in a_turn.universe.planets.itervalues():
            a_planet_report = PlanetReport( self.nation, a_planet )
            self.planets.append( a_planet_report )

    def report_in_text( self ):
        """Create a plain text turn report from all
        the information in this report.
        """
        pass

