#! /usr/bin/env python
"""
http://oj.leetcode.com/problems/reverse-integer/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Since Apr-09-2014 17:02
"""

class Solution:
    # @return an integer
    def reverse(self, x):
        if x >=0:
            return int(''.join(reversed(str(x))))
        else:
            return -int(''.join(reversed(str(-x))))

if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
