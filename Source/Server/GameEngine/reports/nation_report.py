
class NationReport(object):

    def __init__( self, a_nation, a_turn ):
        self.name = a_nation.name
        self.population = 0
        self.industry   = 0
        self.drive_tech   = a_nation.drive_tech
        self.weapons_tech = a_nation.weapons_tech
        self.shield_tech  = a_nation.shield_tech
        self.cargo_tech   = a_nation.cargo_tech

        for p in a_turn.universe.occupied_planets():
            if p.is_owner( a_nation ) :
                self.population = self.population + p.population
                self.industry   = self.industry   + p.industry

