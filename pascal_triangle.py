#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/pascals-triangle/

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Since Apr-22-2014 18:46
"""


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            init = self.generate(numRows - 1)
            prev = init[numRows - 2]
            last = [1]
            for i in range(len(prev) - 1):
                last.append(prev[i] + prev[i + 1])
            last.append(1)
            init.append(last)
            return init

if __name__ == '__main__':
    s = Solution()
    assert s.generate(0) == []
    assert s.generate(1) == [[1]]
    assert s.generate(2) == [[1], [1, 1]]
    assert s.generate(3) == [[1], [1, 1], [1, 2, 1]]
    num = 8
    for x in s.generate(num):
        print(x)
