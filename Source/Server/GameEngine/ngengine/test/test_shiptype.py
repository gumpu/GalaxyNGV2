from ngengine.elements.shiptype import Shiptype
from math import isclose


def test_mass():
    drone = Shiptype(0, "drone", 1, 0, 0, 0, 0)
    flak = Shiptype(0, "flak", 1, 0, 0, 2, 0)
    destroyer = Shiptype(0, "destroyer", 6, 3, 4, 4, 0)
    freighter = Shiptype(0, "freighter", 30.00, 0, 0.00, 9.50, 10.00)

    assert isclose(drone.mass(), 1.0)
    assert isclose(flak.mass(), 3.0)
    assert isclose(destroyer.mass(), 18.0)
    assert isclose(freighter.mass(), 49.50)


if __name__ == "__main__":
    pass

# --------------- end of file -----------------------------------------
