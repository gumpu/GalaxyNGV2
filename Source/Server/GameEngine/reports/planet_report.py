# vi: spell spl=en

class PlanetReport(object):
    def __init__( self, a_turn, a_nation, a_planet ):
        self.name      = a_planet.name
        self.x         = a_planet.x
        self.y         = a_planet.y
        self.owner     = None
        self.size      = None
        self.resources = None

class OccupiedPlanetReport( PlanetReport ):
    def __init__( self, a_turn, a_nation, a_planet ):
        PlanetReport.__init__( self, a_turn, a_nation, a_planet )
        if a_planet.owner == a_nation.key:
            self.size      = a_planet.size
            self.resources = a_planet.resources

class UnoccupiedPlanetReport( PlanetReport ):
    def __init__( self, a_turn, a_nation, a_planet ):
        PlanetReport.__init__( self, a_turn, a_nation, a_planet )
        self.owner = None
        if a_turn.is_planet_visible( a_planet, a_nation ):
            self.size      = a_planet.size
            self.resources = a_planet.resources

