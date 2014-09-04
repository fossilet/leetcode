#! /usr/bin/env python

"""
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Tue Sep  2 18:33:12 CST 2014
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer

    # FIXME: runtime error on OJ.
    cache = {}

    def memoize(f):
        def inner(*args, **kwargs):
            try:
                return Solution.cache[args[2]]
            except KeyError:
                Solution.cache[args[2]] = f(*args, **kwargs)
                return Solution.cache[args[2]]

        return inner

    def maxProfit(self, prices):
        Solution.cache = {}
        if not prices:
            return 0
        else:
            return max(self.maxProfit1(prices, x) for x in range(len(prices)))

    @memoize
    def maxProfit1(self, prices, x):
        """ Max profit when bying at day x.
        p = a_0, a_1, a_2, ..., a_x, a_x+1, ...
        f(x+1) = max(p[x+2:]) - p[x+1]
        f(x) = max(p[x+1:]) - p(x)
             = max(p[x+1], max(p[x+2:])) - p(x)
             = max(p[x+1], p[x+1] + f(x+1)) - p(x)
        """
        if x == len(prices) - 1:
            return 0
        else:
            return max(prices[x + 1],
                       prices[x + 1] + self.maxProfit1(prices, x + 1)) \
                   - prices[x]


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 8, 4]
    assert [s.maxProfit1(a, x) for x in range(len(a))] == [7, 6, 5, -4, 0]

    a = []
    assert s.maxProfit(a) == 0
    a = [1]
    assert s.maxProfit(a) == 0
    a = [1, 1, 1, 1, 1]
    assert s.maxProfit(a) == 0
    a = [1, 2, 3, 8, 4]
    assert s.maxProfit(a) == 7
    a = [1, 2, 3, 4, 5]
    assert s.maxProfit(a) == 4
    a = [5, 4, 3, 2, 1]
    assert s.maxProfit(a) == 0
