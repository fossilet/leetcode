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
    def maxProfit(self, prices):
        if not prices:
            return 0
        else:
            m = min(prices) - max(prices)
            # FIXME: O(n^2) is too slow for OJ.
            for i in range(len(prices)):
                for j in range(i + 1, len(prices)):
                    cur = prices[j] - prices[i]
                    if cur > m:
                        m = cur
            return m

if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 8, 4]
    assert s.maxProfit(a) == 7
    a = [5, 4, 3, 2, 1]
    assert s.maxProfit(a) == -1
    a = [1, 2, 3, 4, 5]
    assert s.maxProfit(a) == 4
    a = [1, 1, 1, 1, 1]
    assert s.maxProfit(a) == 0
