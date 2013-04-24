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
        for i in xrange(0, options.number_of_nations):
            name = "Nation_%d" % (i+1)
            a_nation = Nation( ukey.next(), name ) 
            self.nations[a_nation.key] = a_nation
        self.universe = Universe()
        self.universe.create( options )

    def report( self ):
        self.universe.report()

