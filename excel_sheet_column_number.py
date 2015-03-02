"""
https://oj.leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        l = len(s)
        n = 0
        for i in range(l):
            n += (ord(s[i]) - ord('A') + 1) * 26 ** (l - i - 1)
        return n

if __name__ == '__main__':
    s = Solution()
    assert s.titleToNumber('A') == 1
    assert s.titleToNumber('Z') == 26
    assert s.titleToNumber('AA') == 27
    assert s.titleToNumber('BAC') == 1381
