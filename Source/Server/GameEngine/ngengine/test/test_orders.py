from ngengine.game import Game
from ngengine.orders import OrderList
from ngengine.creation_options import CreationOptions


def test_production():
    options = CreationOptions()
    a_game = Game()
    a_game.create(options)
    order = "produce 1 cap"
    a_turn = a_game.turn[0]
    nation = a_turn.get_nation("Nation_1")
    assert nation is not None
    orderlist = OrderList(nation)
    orderlist.add(order)


if __name__ == "__main__":
    pass
# --------------- end of file -----------------------------------------
