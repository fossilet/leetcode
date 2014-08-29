#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/remove-element/

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Since Apr-22-2014 15:44
"""


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        B = list(A)
        for i in B:
            if i == elem:
                A.remove(elem)
        return len(A)

if __name__ == '__main__':
    s = Solution()
    A = [4, 5]
    print(s.removeElement(A, 4))
