#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/single-number-ii/

Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Since Apr-15-2014 18:31
"""

import collections


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = collections.defaultdict(int)
        for x in A:
            dic[x] += 1
        for k in dic:
            if dic[k] != 3:
                return k
