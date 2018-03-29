#!/usr/bin/env python
# vi: spell spl=en
#

import unittest
from   ngengine.orders import Orders

class OrdersTestCase(unittest.TestCase):
    def test_dummy(self):
        pass

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OrdersTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)


