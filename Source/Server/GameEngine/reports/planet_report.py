# vi: spell spl=en

class PlanetReport(object):

    def __init__( self, a_turn, a_nation, a_planet ):
        self.name      = a_planet.name
        self.x         = a_planet.x
        self.y         = a_planet.y
        self.owner     = a_turn.planet_owner( a_planet )
        self.size      = None
        self.resources = None
