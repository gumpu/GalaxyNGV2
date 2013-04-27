#!/usr/bin/python -3
# vi: spell spl=en

import itertools

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
            a_planet_report = PlanetReport( a_turn, self.nation, a_planet )
            self.planets.append( a_planet_report )

    def report_in_text( self, report_file ):
        """Create a plain text turn report from all
        the information in this report.
        """
        report_file.write( 'Unoccupied Planets\n' )
        report_file.write( 'x,y,size,resources\n' )
        for i in itertools.ifilter( lambda p: p.owner == 'Unoccupied', self.planets ):
            report_file.write( "{0},{1},{2},{3},{4}\n".format( 
                i.name, i.x, i.y, i.size, i.resources ) )
