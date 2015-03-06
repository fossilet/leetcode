"""
https://oj.leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for x in s:
            if x in '({[':
                stack.append(x)
            else:
                try:
                    y = stack.pop()
                except IndexError:
                    return False
                if not ((x == '(' and y == ')') or (x == '[' and y == ']') or (x == '{' and y == '}') or
                        (y == '(' and x == ')') or (y == '[' and x == ']') or (y == '{' and x == '}')):
                    return False
        return stack == []


if __name__ == '__main__':
    s = Solution()
    assert s.isValid('()')
    assert s.isValid('[]')
    assert not s.isValid('[')
    assert not s.isValid('}')
    assert not s.isValid('([')
    assert s.isValid('([]{})[]')
    assert not s.isValid('([)]')
