#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Since Apr-22-2014 18:16
"""


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        L = len(A)
        if L in (0, 1):
            return L
        else:
            i = 0
            while i <= L - 2:
                if A[i] == A[i + 1]:
                    A.remove(A[i])
                L = len(A)
                i += 1
            return len(A)

if __name__ == '__main__':
    s = Solution()

    A = []
    assert s.removeDuplicates(A) == 0
    assert A == []

    A = [1]
    assert s.removeDuplicates(A) == 1
    assert A == [1]

    A = [1, 1, 2]
    assert s.removeDuplicates(A) == 2
    assert A == [1, 2]

    A = [1, 1, 2, 3, 4, 4, 5, 5]
    assert s.removeDuplicates(A) == 5
    assert A == [1, 2, 3, 4, 5]

    A = [1, 2, 3, 4, 5]
    assert s.removeDuplicates(A) == 5
    assert A == [1, 2, 3, 4, 5]
