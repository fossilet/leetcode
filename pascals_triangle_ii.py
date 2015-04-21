"""
https://leetcode.com/problems/pascals-triangle-ii/

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

from math import factorial as f


class Solution:
    # @param rowIndex, an integer
    # @return an integer[]
    def getRow(self, rowIndex):
        c = lambda n, m: f(n) / f(m) / f(n - m)
        return [c(rowIndex, m) for m in range(rowIndex + 1)]


if __name__ == '__main__':
    s = Solution()
    assert [s.getRow(i) for i in range(8)] == [[1],
                                             [1, 1],
                                            [1, 2, 1],
                                           [1, 3, 3, 1],
                                          [1, 4, 6, 4, 1],
                                        [1, 5, 10, 10, 5, 1],
                                       [1, 6, 15, 20, 15, 6, 1],
                                     [1, 7, 21, 35, 35, 21, 7, 1]]
