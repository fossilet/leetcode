"""
https://oj.leetcode.com/problems/roman-to-integer/

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    # @return an integer
    mapping = {
        '': 0,
        None: 0,
        'MMM': 3000,
        'MM': 2000,
        'M': 1000,

        'CM': 900,
        'DCCC': 800,
        'DCC': 700,
        'DC': 600,
        'D': 500,
        'CD': 400,
        'CCC': 300,
        'CC': 200,
        'C': 100,

        'XC': 90,
        'LXXX': 80,
        'LXX': 70,
        'LX': 60,
        'L': 50,
        'XL': 40,
        'XXX': 30,
        'XX': 20,
        'X': 10,

        'IX': 9,
        'VIII': 8,
        'VII': 7,
        'VI': 6,
        'V': 5,
        'IV': 4,
        'III': 3,
        'II': 2,
        'I': 1
    }

    def romanToInt(self, s):
        import re

        a = '(M{0,3})?'
        b = '((CM)|(DC{0,3})|(CD)|(C{1,3}))?'
        c = '((XC)|(LX{0,3})|(XL)|(X{1,3}))?'
        d = '((IX)|(VI{0,3})|(IV)|(I{1,3}))?'
        m = re.match(a + b + c + d, s)
        mm = [Solution.mapping[x] for x in
              m.group(1), m.group(2), m.group(7), m.group(12)]
        return reduce(int.__add__, mm)


if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt('MCMIV') == 1904
    assert s.romanToInt('MMMCMXCIX') == 3999
    assert s.romanToInt('DCXXI') == 621
