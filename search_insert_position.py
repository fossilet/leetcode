#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

Since Apr-15-2014 18:02
"""


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        pos = 0
        for i in range(len(A)):
            if target <= A[i]:
                return i
        else:
            return len(A)

if __name__ == '__main__':
    s = Solution()
    A = [1, 3, 5, 6]
    assert s.searchInsert(A, 5) == 2
    assert s.searchInsert(A, 2) == 1
    assert s.searchInsert(A, 7) == 4
    assert s.searchInsert(A, 0) == 0
