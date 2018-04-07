# vi: spell spl=en

class PlanetReport(object):
    def __init__( self, a_turn, a_nation, a_planet ):
        self.name      = a_planet.name
        self.x         = a_planet.x
        self.y         = a_planet.y
        self.owner     = None
        self.size      = None
        self.resources = None
        self.population = None
        self.colonists = None

class OccupiedPlanetReport( PlanetReport ):
    def __init__( self, a_turn, a_nation, a_planet ):
        PlanetReport.__init__( self, a_turn, a_nation, a_planet )
        if ( (a_planet.owner == a_nation.key) or
             a_turn.is_planet_visible( a_planet, a_nation ) ):
            self.owner     = a_planet.owner
            self.size      = a_planet.size
            self.resources = a_planet.resources
            self.population = a_planet.population
            self.industry   = a_planet.industry
            self.capital    = a_planet.capital
            self.materials  = a_planet.materials
            self.colonists  = a_planet.colonists
        else:
            self.owner     = None   # Which means unknown, not visible.


class UnoccupiedPlanetReport( PlanetReport ):
    def __init__( self, a_turn, a_nation, a_planet ):
        PlanetReport.__init__( self, a_turn, a_nation, a_planet )
        self.owner = None
        if a_turn.is_planet_visible( a_planet, a_nation ):
            self.size      = a_planet.size
            self.resources = a_planet.resources

