# Since Mon Mar  2 17:00:43 CST 2015
"""
https://oj.leetcode.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        i = -1
        length = 0

        while i >= -len(s):
            if s[i] == ' ':
                if length == 0:
                    i -= 1
                    continue
                else:
                    break
            else:
                length += 1
                i -= 1
        return length

if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLastWord(' ') == 0
    assert s.lengthOfLastWord('   ') == 0
    assert s.lengthOfLastWord('s') == 1
    assert s.lengthOfLastWord('s ') == 1
    assert s.lengthOfLastWord('  s   ') == 1
    assert s.lengthOfLastWord('Hello world') == 5
    assert s.lengthOfLastWord('Hello ') == 5
