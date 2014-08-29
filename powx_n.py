#! /usr/bin/env python

"""
http://oj.leetcode.com/problems/powx-n/

Implement pow(x, n).

Since Apr-22-2014 19:09
"""


class Solution:
    # @param x, a float
    # @param n, an integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            # Do not misuse the builtin pow.
            a = self.pow(x, n / 2)
            return a * a
        elif n > 0:
            return x * self.pow(x, n - 1)
        else:
            # avoid Python 2 division bug
            return self.pow(x, n + 1) * 1.0 / x


if __name__ == '__main__':
    s = Solution()
    assert s.pow(2, 0) == 1
    assert s.pow(0.2, 1) == 0.2
    assert s.pow(-2, 2) == 4
    assert s.pow(2, 3) == 8
    assert s.pow(2, 6) == 64
    assert s.pow(2, 12) == 4096
    assert abs(s.pow(-3, -3) + 0.037037) < 10e-5
