#! /usr/bin/env python

"""
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Tue Sep  2 18:33:12 CST 2014
"""
import unittest


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        """ Directly converted from the recursion version.
        """
        i = len(prices) - 1
        res = 0
        t = 0  # tentative
        while i > 0:
            t = max(prices[i - 1], prices[i] + t) - prices[i - 1]
            i -= 1
            if t > res:
                res = t
        return res

    def __init__(self):
        self.cache = {}

    def memoize(f):
        # Note: `f' is the wrapped function, not an `self' instance.
        def inner(*args, **kwargs):
            try:
                return args[0].cache[args[2]]
            except KeyError:
                args[0].cache[args[2]] = f(*args, **kwargs)
                return args[0].cache[args[2]]
        return inner

    def maxProfit_recursion(self, prices):
        if not prices:
            return 0
        else:
            return max(self.profit_helper(prices, x) for x in range(len(prices)))

    @memoize
    # NOTE: memoize cannot avoid recursion limit exception.
    def profit_helper(self, prices, x):
        """ Max profit when bying at day x.
        p = a_0, a_1, a_2, ..., a_x, a_x+1, ...
        f(x+1) = max(p[x+1:]) - p[x+1]
        f(x) = max(p[x:]) - p(x)
             = max(p[x], max(p[x+1:])) - p(x)
             = max(p[x], p[x+1] + f(x+1)) - p(x)
        """
        if x == len(prices) - 1:
            return 0
        else:
            return max(prices[x],
                       prices[x + 1] + self.profit_helper(prices, x + 1)) \
                   - prices[x]


class testSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_profithelper(self):
        a = [1, 2, 3, 8, 4]
        self.assertEqual([self.s.profit_helper(a, x) for x in range(len(a))],
                         [7, 6, 5, 0, 0])

    def test_profithelper1(self):
        a = [5, 4, 3, 2, 1]
        self.assertEqual([self.s.profit_helper(a, x) for x in range(len(a))],
                         [0, 0, 0, 0, 0])

    def test_maxProfit(self):
        self.assertEqual(self.s.maxProfit([]), 0)
        self.assertEqual(self.s.maxProfit_recursion([]), 0)

    def test_maxProfit1(self):
        self.assertEqual(self.s.maxProfit([1]), 0)
        self.assertEqual(self.s.maxProfit_recursion([]), 0)

    def test_maxProfit2(self):
        self.assertEqual(self.s.maxProfit([1, 1, 1, 1, 1]), 0)
        self.assertEqual(self.s.maxProfit_recursion([]), 0)

    def test_maxProfit3(self):
        self.assertEqual(self.s.maxProfit([1, 2, 3, 8, 4]), 7)
        self.assertEqual(self.s.maxProfit_recursion([]), 0)

    def test_maxProfit4(self):
        self.assertEqual(self.s.maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.s.maxProfit_recursion([]), 0)

    def test_maxProfit5(self):
        self.assertEqual(self.s.maxProfit([5, 4, 3, 2, 1]), 0)
        self.assertEqual(self.s.maxProfit_recursion([]), 0)


if __name__ == '__main__':
    unittest.main()
