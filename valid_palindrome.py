"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        import string

        ss = []
        for c in s:
            if c in string.letters or c in string.digits:
                ss.append(c.lower())
        l = len(ss)
        if l == 0:
            return True
        else:
            for i in range(l / 2):
                if ss[i] != ss[l - 1 - i]:
                    return False
            else:
                return True


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome('')
    assert s.isPalindrome('1')
    assert s.isPalindrome('11')
    assert not s.isPalindrome('sb')
    assert s.isPalindrome("A man, a plan, a canal: Panama")
    assert not s.isPalindrome("race a car")
