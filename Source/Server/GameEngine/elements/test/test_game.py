#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from elements.game import Game


class GameTestCase(unittest.TestCase):

    def test_create_game(self):
        a_game = Game()
        a_game.create(None)
        self.assertIsEqual(a_game.turn, 1 )

    def test_dummy(self):
        pass

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GameTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

