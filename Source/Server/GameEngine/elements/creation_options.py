# vi: spell spl=en

class CreationOptions(object):

    """Set of parameters that define how a game
    is to be created at turn 0.
    """
    def __init__( self ):
        self.number_of_nations = 4
        self.number_of_empty_planets = 10
        self.universe_size = 400
