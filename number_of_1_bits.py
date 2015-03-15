# coding=utf-8
"""
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return sum(1 for c in bin(n)[2:] if c == '1')


if __name__ == '__main__':
    s = Solution()
    assert s.hammingWeight(0) == 0
    assert s.hammingWeight(11) == 3
    assert s.hammingWeight(511) == 9
