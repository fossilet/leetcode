#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/powx-n/

Implement pow(x, n).

Since Apr-22-2014 19:09
"""


class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        else:
            return x * pow(x, n - 1)
