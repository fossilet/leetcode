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
        return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1)
                   if prices[i + 1] - prices[i] > 0)


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
