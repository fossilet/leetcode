"""
https://oj.leetcode.com/problems/implement-strstr/

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        else:
            i, j, ind = 0, 0, 0
            while i < len(needle) and j < len(haystack):
                if needle[i] == haystack[j]:
                    i += 1
                    j += 1
                    ind += 1
                    if ind == len(needle):
                        return j - ind
                else:
                    j -= ind - 1
                    i = 0
                    ind = 0
            else:
                return -1


if __name__ == '__main__':
    s = Solution()
    assert s.strStr('abcdefg', 'abc') == 0
    assert s.strStr('abdefg', 'abc') == -1
    assert s.strStr('abdefgabc', 'abc') == 6
    assert s.strStr('', '') == 0
    assert s.strStr('', 'a') == -1
    assert s.strStr("mississippi", "issip") == 4

