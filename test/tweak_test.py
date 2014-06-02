from operator import mul
import unittest

from data_access import get_file
from stress import point_tweak


__author__ = 'andriod'


class PointTestCase(unittest.TestCase):
    def test_point_tweak(self):
        market = get_file("market1")
        preTweak = market.fx.usd_eur.Rate['2010-5-14']
        tweakedMarket = point_tweak(market, 'fx.usd_eur.Rate', '2010-5-14', mul, 1.1)
        postTweak = tweakedMarket.fx.usd_eur.Rate['2010-5-14']
        self.assertAlmostEqual(preTweak * 1.1, postTweak)


if __name__ == '__main__':
    unittest.main()
