
import unittest
from ngengine.ukey import UKey
from ngengine.creation_options import CreationOptions
from ngengine.turn import Turn

def count_them( an_iterator ):
    n = 0
    for i in an_iterator:
        n = n + 1
    return n

class TurnTestCase(unittest.TestCase):

    def test_create( self ):
        """Create a universe and see if it matches the creation parameters
        """
        options = CreationOptions()
        ukey = UKey()
        turn = Turn()
        turn.create( options, ukey )
        self.assertEqual( 
               count_them( turn.universe.all_planets() ),
               options.number_of_nations +
               options.number_of_stuff_planets )
        self.assertEqual(
               count_them( turn.universe.unoccupied_planets() ),
               options.number_of_stuff_planets )

        self.assertEqual(
               count_them(turn.all_nations()),
               options.number_of_nations)

        nations = turn.all_nations()
        self.assertEqual(nations[0].drive_tech, 1.0)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TurnTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
