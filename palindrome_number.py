"""
https://oj.leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. Do this without extra space.
"""


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            l = Solution.get_len(x)
            for i in range(l / 2):
                fst, x = divmod(x, 10 ** (l - 2 * i - 1))
                x, last = divmod(x, 10)
                if fst != last:
                    return False
            else:
                return True

    @staticmethod
    def get_len(x):
        """Get length of int x."""
        if x == 0:
            return 1
        else:
            l = 0
            while x != 0:
                x /= 10
                l += 1
            return l


if __name__ == '__main__':
    s = Solution()
    assert s.get_len(0) == 1
    assert s.get_len(3) == 1
    assert s.get_len(333) == 3
    assert s.get_len(13254) == 5
    assert s.isPalindrome(0)
    assert s.isPalindrome(1)
    assert s.isPalindrome(131)
    assert s.isPalindrome(1331)
    assert s.isPalindrome(1318131)
    assert not s.isPalindrome(23)
    assert not s.isPalindrome(13254)
    assert not s.isPalindrome(-2147483648)
    assert not s.isPalindrome(-2147447412)
