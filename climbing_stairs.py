#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Since Apr-15-2014 19:06
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        # if n == 1 or n == 2:
        #     return n
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        a, b = 1, 2
        if n == 1 or n == 2:
            return n
        else:
            for i in range(n - 2):
                a, b = b, a + b
            return b
