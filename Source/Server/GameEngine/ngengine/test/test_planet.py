from ngengine.elements.planet import Planet, PROD_CAPITAL
from math import isclose


def test_population_growth():
    """TODO Population growth"""
    assert True  # TODO


def test_is_occupied():
    """Is planet occupied test"""
    p = Planet("Test")
    assert not p.is_occupied()
    p.owner = 1
    assert p.is_occupied()


def test_capital_production():
    """Production of capital for various planet sizes"""
    p = Planet("Test")
    p.population = 1000.0
    p.industry = 1000.0
    p.resources = 10.0
    p.product = PROD_CAPITAL

    p.produce()
    assert isclose(p.capital, 196.08, abs_tol=0.005)

    p2 = Planet("2")
    p2.population = 1000.0
    p2.industry = 1000.0
    p2.resources = 10.0
    p2.materials = 200
    p2.product = PROD_CAPITAL

    p2.produce()
    assert isclose(p2.capital, 200)

    p3 = Planet("3")
    p3.population = 1000.0
    p3.industry = 1000.0
    p3.resources = 0.1
    p3.materials = 0
    p3.product = PROD_CAPITAL

    p3.produce()
    assert isclose(p3.capital, 66.67, abs_tol=0.005)


if __name__ == "__main__":
    pass

# --------------- end of file -----------------------------------------
