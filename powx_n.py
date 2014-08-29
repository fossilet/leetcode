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
        elif n == 1:
            return x
        elif n % 2 == 0:
            return pow(x, n / 2) * pow(x, n / 2)
        else:
            return x * pow(x, n - 1)

if __name__ == '__main__':
    assert pow(2, 0) == 1
    assert pow(0.2, 1) == 0.2
    assert pow(-2, 2) == 4
    assert pow(2, 3) == 8
    assert pow(2, 6) == 64
    assert pow(2, 12) == 4096
