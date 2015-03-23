"""
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        s = 0
        k = 1
        while 5 ** k <= n:
            s += n / 5 ** k
            k += 1
        return s


if __name__ == '__main__':
    s = Solution()
    assert s.trailingZeroes(5) == 1
    assert s.trailingZeroes(70) == 16
