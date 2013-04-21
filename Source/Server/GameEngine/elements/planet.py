# vi: spell spl=en


PROD_CAPITAL  = 1
PROD_SHIP     = 2
PROD_MATERIAL = 3
PROD_DRIVE    = 4
PROD_WEAPONS  = 5
PROD_SHIELD   = 6
PROD_CARGO    = 7

MAT_PER_CAP   = 1.0  # Materials needed per unit of capital
IND_PER_CAP   = 5.0  # Industry needed per unit of capital

class Planet(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.name = name
        self.size = 0
        self.population = 0
        self.industry   = 0
        self.production = None
        self.resources  = 0
        # Stockpiles
        self.materials  = 0
        self.colonists  = 0
        self.capital    = 0


    """Compute the distance between this planet and
    another planet.
    """
    def dist(self, another_planet):
        return 0


    """Gives a unique key that says the same during
    the whole game.
    """
    def key(self):
        k = "%d,%d" % (self.x, self.y)
        return k

    def report(self):
        print ( "%s %d %d" % (self.name, self.x, self.y) )


    def produce(self):

        industry = self.industry*0.75 + self.population*0.25

        if self.production   == PROD_MATERIAL:
            self.materials = self.materials + industry * self.resources
        elif self.production == PROD_SHIP:
            pass
        elif self.production == PROD_CAPITAL:
            material_demand = industry / IND_PER_CAP
            if material_demand > self.materials:
                # First use the existing resources to build capital
                capital = self.materials * MAT_PER_CAP
                industry = industry - capital * IND_PER_CAP
                self.materials = 0
                # The build more material and use that to build capital
                capital = capital + industry / (IND_PER_CAP + 1.0 / self.resources)
            else:
                capital = self.materials * MAT_PER_CAP
                industry = industry - capital * IND_PER_CAP
                self.materials = self.materials - material_demand
            self.capital = self.capital + capital
        else:
            pass

