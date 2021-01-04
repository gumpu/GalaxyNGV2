from ngengine.game import Game
from ngengine.universe import Universe, distance, PlanetPlacementError
from ngengine.elements.planet import Planet


def test_place_planet():
    """Trying adding 40 planets in a large universe"""
    universe = Universe()
    universe.size = 500
    for n in range(0, 40):
        a_planet = Planet(name="test")
        universe.place_planet(a_planet)
        universe.add_planet(a_planet)
    assert len(universe.planets) == 40


def test_place_planet_exception():
    """Trying to add to many planets should fail"""
    universe = Universe()
    universe.size = 5  # So no more than 36 planets can fit


# FIXME
#    with self.assertRaises(PlanetPlacementError):
#        # This should raise an exception
#        for n in range(0, 40):
#            a_planet = Planet(name='test')
#           universe.place_planet(a_planet)
#           universe.add_planet(a_planet)


def test_distance():
    """Computing distances between planets"""
    p1 = Planet("1")
    p2 = Planet("2")
    assert distance(p1, p2) == 0
    p1.x = 40
    assert distance(p1, p2) == 40
    p2.x = 40
    assert distance(p1, p2) == 0
    p2.y = 80
    assert distance(p1, p2) == 80


if __name__ == "__main__":
    pass

# --------------- end of file -----------------------------------------
