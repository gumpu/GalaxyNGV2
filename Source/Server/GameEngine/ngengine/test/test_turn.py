from ngengine.ukey import UKey
from ngengine.creation_options import CreationOptions
from ngengine.turn import Turn


def count_them(an_iterator):
    n = 0
    for i in an_iterator:
        n = n + 1
    return n


def test_create():
    """Create a universe and see if it matches the creation parameters"""
    options = CreationOptions()
    ukey = UKey()
    turn = Turn()
    turn.create(options, ukey)
    assert (
        count_them(turn.universe.all_planets())
        == options.number_of_nations + options.number_of_stuff_planets
    )
    assert (
        count_them(turn.universe.unoccupied_planets())
        == options.number_of_stuff_planets
    )
    assert count_them(turn.all_nations()) == options.number_of_nations

    nations = turn.all_nations()
    for n in nations:
        assert n.drive_tech == 1.0


if __name__ == "__main__":
    pass
# --------------- end of file -----------------------------------------
