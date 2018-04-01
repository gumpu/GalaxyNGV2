#!/usr/bin/env python

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

    def test_run_game(self):
        """Test running a games"""
        options = CreationOptions()
        a_game = Game()
        # Create first turn
        a_game.create(options)
        # Compute next turn
        a_game.run(None)

        # There should be a new turn now.
        self.assertEqual(len(a_game.turn), 2)

        old_turn = a_game.turn[-2]
        new_turn = a_game.turn[-1]
        old_occupied_planets = old_turn.universe.occupied_planets()
        new_occupied_planets = new_turn.universe.occupied_planets()
        # The number of occupied planets should be the same.
        self.assertEqual(len(old_occupied_planets), len(new_occupied_planets))

        n1 = new_occupied_planets[1]
        o1 = old_occupied_planets[1]
        self.assertNotEqual(n1, o1)
        self.assertNotEqual(n1.colonists, o1.colonists)


if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GameTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

