"""
https://oj.leetcode.com/problems/plus-one/

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        return [int(x) for x in str(int(''.join(str(x) for x in digits)) + 1)]


if __name__ == '__main__':
    s = Solution()
    assert s.plusOne([0]) == [1]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([1, 3, 4, 9]) == [1, 3, 5, 0]
