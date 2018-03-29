# vi: spell spl=en

from ngengine.universe import Universe
from ngengine.elements.nation import Nation
import random


class Turn(object):
    """All data for a single turn.
    """
    def __init__( self ):
        self.universe = Universe()
        self.nations  = {}
        self.number   = 0

    def create( self, options, ukey ):
        """The big bang, this makes the turn 0 data.

        Create the universe, nations, and a whole bunch of planets.
        """
        # Create all nations.
        for i in range( 0, options.number_of_nations ):
            name = "Nation_%d" % (i+1)
            a_nation = Nation(next(ukey), name) 
            self.nations[a_nation.key] = a_nation
        # Now create all planets
        self.universe.create(options, self.nations)

    def all_nations( self ):
        return self.nations.values()

    def planet_owner(self, a_planet):
        """Find the name of the nation that owns the given
        planet if any.

        Return the name of the owner, or 'Unoccupied'.
        """
        if a_planet.owner in self.nations :
            owner_name = self.nations[ a_planet.owner ].name
        else:
            owner_name = 'Unoccupied'

        return owner_name

    def map( self, file ):
        """Write a csv file with data on all planets
        that can be used to create a map.

        For debugging and development.
        """
        self.universe.map( file, self )

    def is_planet_visible( self, a_planet, a_nation ):
        """Is the given planet visible to the nation?

        This can be because the nations owns the planet,
        or has a group orbiting the planet.
        """
        return random.random() < 0.5  # TODO, this is just for testing.

    def is_group_visible( self, a_group, a_nation ):
        """Is the given group visible to the nation?

        This can be because the nation owns the group
        or has a group orbiting the same planet as
        the group is orbiting.
        """
        return True # TODO

