# vi: spell spl=en

import random

# The products a planet can produce.
PROD_CAPITAL  = 1
PROD_SHIP     = 2
PROD_MATERIAL = 3
PROD_DRIVE    = 4
PROD_WEAPONS  = 5
PROD_SHIELD   = 6
PROD_CARGO    = 7

# Production constants.
MAT_PER_CAP   = 1.0  # Materials needed per unit of capital
IND_PER_CAP   = 5.0  # Industry needed per unit of capital

POPULATION_GROWTH_FACTOR = 1.08 # Population grow by 8% each turn

POP_PER_COL   = 8 # 8 people are turned into one colonist.

class Planet(object):

    """Planet -- base class for a kinds of planets
    """
    def __init__( self, name ):
        self.x = 0    # Integer  | x and y are used as a key
        self.y = 0    # Integer  | so we can't have floats here.
        self.name = name
        self.size = 0
        self.population = 0
        self.industry   = 0
        self.product    = None
        self.resources  = 0
        # Stockpiles
        self.materials  = 0
        self.colonists  = 0
        self.capital    = 0
        self.owner      = None   # Nation key or None

    def create_primary( self ):
        self.size       = 1000
        self.population = 1000
        self.resources  = 10

    def create_stuff( self ):
        self.size      = random.randint( 10, 300 )
        self.resources = random.expovariate( 1 )

    """Gives a unique key that says the same during
    the whole game.
    """
    def key( self ):
        k = "%d,%d" % (self.x, self.y)  # TODO use format
        return k

    def is_occupied( self ):
        """Is this planet occupied by a nation?
        """
        return self.owner is not None

    def is_owner( self, a_nation ):
        """Is the given nation the owner of this planet?
        """
        return self.owner == a_nation.key

    def grow_population( self ):
        self.population = self.population * POPULATION_GROWTH_FACTOR
        if self.population > self.size :
            surplus = self.population - self.size
            self.population = self.size
            self.colonists = surplus / POP_PER_COL

    def grow_industry( self ):
        pass

    def produce( self ):
        """Let the planet produce the set product.

        Possible products are:
        Capital, material, ship, or technology.
        """
        industry = self.industry * 0.75 + self.population * 0.25

        if self.product   == PROD_MATERIAL:
            self.materials = self.materials + industry * self.resources
        elif self.product == PROD_SHIP:
            pass
        elif self.product == PROD_CAPITAL:
            material_demand = industry / IND_PER_CAP
            if material_demand > self.materials:
                # First use the existing resources to build capital
                capital = self.materials * MAT_PER_CAP
                industry = industry - capital * IND_PER_CAP
                self.materials = 0
                # Then use the remaining industry to build some more material 
                # and use that to build capital
                capital = capital + industry / (IND_PER_CAP + 1.0 / self.resources)
            else:
                capital = self.materials * MAT_PER_CAP
                industry = industry - capital * IND_PER_CAP
                self.materials = self.materials - material_demand
            self.capital = self.capital + capital
        else:
            pass

