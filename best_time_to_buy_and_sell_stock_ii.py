#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
Since Apr-09-2014 18:59
"""


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        i, j = 0, 1
        n = len(prices)
        p = 0
        while i < n and j < n:
            if prices[j] > prices[i]:
                p += prices[j] - prices[i]
            i += 1
            j += 1
        return p


if __name__ == '__main__':
    s = Solution()
    p = [1, 3, 2, 4]
    assert s.maxProfit(p) == 4
    p = [4, 3, 2, 1]
    assert s.maxProfit(p) == 0
    p = [1, 1]
    assert s.maxProfit(p) == 0
    p = [1]
    assert s.maxProfit(p) == 0
