#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
import pickle
from ngengine.game import Game
from ngengine.creation_options import CreationOptions

class GameTestCase(unittest.TestCase):

    def test_create_game(self):
        options = CreationOptions()
        a_game = Game()
        a_game.create(options)
        self.assertEqual(len(a_game.turn), 1)
        self.assertEqual(len(a_game.turn[0].nations), options.number_of_nations)

    def test_save_game(self):
        """Test consistency of saving and loading games"""
        options = CreationOptions()
        a_game = Game()
        a_game.create(options)
        k = a_game.ukey.next()
        self.assertGreater(k, 1)
        k2 = a_game.ukey.next()
        self.assertGreater(k2, k)
        with open('/tmp/test.pickel', 'wb') as f :
            pickle.dump(a_game, f, pickle.HIGHEST_PROTOCOL)

        with open('/tmp/test.pickel', 'rb') as f :
            a_game_2 = pickle.load(f)

        k3 = a_game_2.ukey.next()
        self.assertGreater(k3, k2)
        self.assertEqual(len(a_game.turn), 1)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GameTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

