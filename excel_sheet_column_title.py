"""
https://oj.leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution:
    # @return a string
    def convertToTitle(self, num):
        l = []
        a = ord('A')
        while num != 0:
            num, r = divmod(num, 26)
            if r != 0:
                l.insert(0, chr(r + a - 1))
            else:
                l.insert(0, 'Z')
                num -= 1

        return ''.join(l)


if __name__ == '__main__':
    s = Solution()
    assert s.convertToTitle(1) == 'A'
    assert s.convertToTitle(26) == 'Z'
    assert s.convertToTitle(27) == 'AA'
    assert s.convertToTitle(1381) == 'BAC'
