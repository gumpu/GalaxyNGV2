#!/usr/bin/python -3
# vi: spell spl=en

import itertools

from ngengine.reports.planet_report import UnoccupiedPlanetReport, OccupiedPlanetReport
from ngengine.reports.nation_report import NationReport


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
        self.unoccupied_planets = []
        self.occupied_planets = []
        # self.battles
        self.nations = []
        # self.messages

    def gather( self, a_turn ):
        """Gather all information for the perspective of the
        nation for which this report is.
        """
        for a_nation in a_turn.all_nations():
            a_nation_report = NationReport( a_nation, a_turn )
            self.nations.append( a_nation_report )

        for a_planet in a_turn.universe.unoccupied_planets():
            a_planet_report = UnoccupiedPlanetReport( 
                    a_turn, self.nation, a_planet )
            self.unoccupied_planets.append( a_planet_report )

        for a_planet in a_turn.universe.occupied_planets():
            a_planet_report = OccupiedPlanetReport( a_turn, self.nation, a_planet )
            self.occupied_planets.append( a_planet_report )

        # Handy to have them sorted, makes reports more readable.
        self.unoccupied_planets = sorted(
                self.unoccupied_planets,
                key=lambda x : '{:>30}'.format(x.name))


    def report_in_text( self, report_file ):
        """Create a plain text turn report from all
        the information in this report.
        """
        report_file.write(
                'Turn {} report for {}\n\n'.format(
                self.turn_number, self.nation.name))

        report_file.write( 'Nations\n' )
        for i in self.nations:
            report_file.write( "{0} {1} {2} {3} {4} {5} {6}\n".format(
                i.name, i.population, i.industry,
                i.drive_tech, i.weapons_tech,
                i.shield_tech, i.cargo_tech ) )
        report_file.write( '\nUnoccupied Planets\n' )
        report_file.write( 'name,x,y,size,resources\n' )
        for i in self.unoccupied_planets:
            report_file.write(
                    #"{0:<4} {1:4} {2:4} {3:4} {4}\n".format(
                    "{0:<4} {1:4} {2} {3} {4}\n".format(
                        i.name, i.x, i.y, i.size, i.resources))

        for a_nation in self.nations:
            found = False
            for i in self.occupied_planets:
                if i.owner == a_nation.key:
                    found = True
                    break
            if found :
                report_file.write(
                        "\n{}'s Planets\n".format( a_nation.name ) )
                for i in self.occupied_planets:
                    if i.owner == a_nation.key :
                        report_file.write(
                            "{0:<4} {1:4} {2:4} {3:4} {4} {5} {6} {7} {8}\n".format( 
                                i.name, i.x, i.y, i.size, i.resources,
                                i.population, i.industry,
                                i.size, i.resources ) )

