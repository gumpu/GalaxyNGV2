# vi: spell spl=en

class CreationOptions(object):

    """Set of parameters that define how a game
    is to be created at turn 0.
    """
    def __init__( self ):
        self.number_of_nations = 8
        self.number_of_empty_planets = 10
        self.universe_size = 400
        # Minimum distance between the primary home planets of any two nations
        self.min_distance = 40

        # The number of smaller empty planets that are scattered around
        # the universe.
        self.number_of_stuff_planets = 100

    def load( filename ):
        """Load the options from file"""
        pass

