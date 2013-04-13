#!/usr/bin/env python

import unittest

suite = unittest.TestLoader().discover('.')
# suite = unittest.TestLoader().loadTestsFromNames(
#         [
#             "elements.test.test_game",
#             "elements.test.test_planet"
#         ] )
unittest.TextTestRunner(verbosity=2).run(suite)

