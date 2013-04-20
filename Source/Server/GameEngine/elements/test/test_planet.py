
# vi: spell spl=en
#

import unittest

class PlanetTestCase(unittest.TestCase):

    def test_key(self):
        pass

    def test_dummy(self):
        pass

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PlanetTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

