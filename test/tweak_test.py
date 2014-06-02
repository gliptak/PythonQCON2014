from operator import mul
import unittest

from data_access import get_file
from stress import point_tweak, step_tweak


__author__ = 'andriod'


class PointTestCase(unittest.TestCase):
    def test_point_tweak(self):
        market = get_file("market1")
        preTweak = market.fx.usd_eur.Rate['2010-5-14']
        preTweakJPY = market.fx.usd_jpy.Rate['2010-5-14']
        tweakedMarket = point_tweak(market, 'fx.usd_eur.Rate', '2010-5-14', mul, 1.1)
        postTweak = tweakedMarket.fx.usd_eur.Rate['2010-5-14']
        postTweakJPY = tweakedMarket.fx.usd_jpy.Rate['2010-5-14']
        self.assertAlmostEqual(preTweak * 1.1, postTweak)
        self.assertAlmostEqual(preTweakJPY, postTweakJPY)


class StepTweakTestCase(unittest.TestCase):
    def test_step_tweak(self):
        market = get_file("market1")
        preTweak = market.fx.usd_eur.Rate['2011-5-13']
        preTweakBefore = market.fx.usd_eur.Rate['2011-5-11']
        preTweakAfter = market.fx.usd_eur.Rate['2011-5-24']
        preTweakJPY = market.fx.usd_jpy.Rate['2011-5-13']
        tweakedMarket = step_tweak(market, 'fx.usd_eur.Rate', '2011-5-12', '2011-5-24', mul, 1.05)
        postTweak = tweakedMarket.fx.usd_eur.Rate['2011-5-13']
        postTweakBefore = market.fx.usd_eur.Rate['2011-5-11']
        postTweakAfter = market.fx.usd_eur.Rate['2011-5-24']
        postTweakJPY = tweakedMarket.fx.usd_jpy.Rate['2011-5-13']
        self.assertAlmostEqual(preTweak * 1.05, postTweak)
        self.assertAlmostEqual(preTweakJPY, postTweakJPY)
        self.assertAlmostEqual(preTweakBefore, postTweakBefore)
        self.assertAlmostEqual(preTweakAfter, postTweakAfter)


if __name__ == '__main__':
    unittest.main()
