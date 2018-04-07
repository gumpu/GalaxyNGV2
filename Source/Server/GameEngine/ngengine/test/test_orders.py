#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from ngengine.game import Game
from ngengine.orders import OrderList
from ngengine.creation_options import CreationOptions

class OrdersTestCase(unittest.TestCase):
    def test_dummy(self):
        pass

    def test_production(self):
        options = CreationOptions()
        a_game = Game()
        a_game.create(options)
        order = "produce 1 cap"
        a_turn = a_game.turn[0]
        nation = a_turn.get_nation("Nation_1")
        self.assertIsNotNone(nation)
        orderlist = OrderList(nation)
        orderlist.add(order)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OrdersTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)


