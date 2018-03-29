
import random
class UKey(object):
    """Unique key generator.
    Used to give all elements in the game a unique id.
    This makes it easier to compute what happened after
    name changes by the players.

    Could have used uuid here, but that would have been
    overkill.
    """
    def __init__(self):
        self.unique_key = 1

    def next(self):
        """Get the next unique key
        """

        # Adding the random element makes it slightly more difficult
        # for a player to gain information about other players
        # from the unique keys.
        self.unique_key = self.unique_key + random.randint(1,5)
        return self.unique_key

