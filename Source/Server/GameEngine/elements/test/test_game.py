#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
import cPickle as p
from elements.game import Game


class GameTestCase(unittest.TestCase):

    def test_create_game(self):
        a_game = Game()
        a_game.create(None)
        self.assertEqual(len(a_game.turn), 1)

    def test_save_game(self):
        """Test consistency of saving and loading games"""
        a_game = Game()
        a_game.create(None)
        k = a_game.ukey.next_key()
        self.assertGreater(k, 1)
        k2 = a_game.ukey.next_key()
        self.assertGreater(k2, k)
        with open('/tmp/test.pickel', 'w') as f :
            p.dump(a_game, f)

        with open('/tmp/test.pickel', 'r') as f :
            a_game_2 = p.load(f)

        k3 = a_game_2.ukey.next_key()
        self.assertGreater(k3, k2)
        self.assertEqual(len(a_game.turn), 1)



if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GameTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

