#! /usr/bin/env python3

"""
Given an array of integers, every element appears twice except for one. Find
that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement
    it without using extra memory?

Tue Apr  8 16:24:46 CST 2014
"""

import collections

class Solution:
    # @param A, a list of integer
    # @return an integer

    def singleNumber(self, A):
        # Don't import collections; it is imported automatically by the OJ.
        dic = collections.defaultdict(int)
        for x in A:
            dic[x] += 1
        for k in dic:
            if dic[k] == 1:
                return k

if __name__ == '__main__':
    li = [1, 2, 3, 4, 3, 4, 2]
    s = Solution()
    print(s.singleNumber(li))
