# coding=utf-8
"""
https://oj.leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        import collections

        count = collections.defaultdict(int)
        for x in num:
            count[x] += 1
        for k, v in count.iteritems():
            if v > len(num) / 2:
                return k


if __name__ == '__main__':
    s = Solution()
    assert s.majorityElement([1, 2, 3, 4, 2, 3, 2, 2]) is None
    assert s.majorityElement([1, 2, 3, 4, 2, 3, 2, 2, 2]) == 2
