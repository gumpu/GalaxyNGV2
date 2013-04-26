# vi: spell spl=en

from elements.universe import Universe
from elements.nation   import Nation

class Turn(object):
    """Data for a single turn
    """

    def __init__( self ):
        self.universe = None
        self.nations  = {}
        self.number   = 0

    def create( self, options, ukey ):
        for i in xrange( 0, options.number_of_nations ):
            name = "Nation_%d" % (i+1)
            a_nation = Nation( ukey.next(), name ) 
            self.nations[ a_nation.key ] = a_nation
        self.universe = Universe()
        self.universe.create( options, self.nations )

    def planet_owner( a_planet ):
        """Find the name of the nation that owns the given
        planet if any.
        """

        if a_planet.owner in nations :
            owner_name = nations[ a_planet.owner ].name
        else:
            owner_name = 'Unoccupied'

        return owner_name


    def report( self ):
        self.universe.report()

    def map( self, file ):
        """Write a csv file with data on all planets
        that can be used to create a map.

        For debugging and development.
        """
        self.universe.map( file, self )

