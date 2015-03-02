"""
https://oj.leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    # @return a string
    def intToRoman(self, num):
        mapping = {
            0: '',
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX',
            90: 'XC',
            100: 'C',
            200: 'CC',
            300: 'CCC',
            400: 'CD',
            500: 'D',
            600: 'DC',
            700: 'DCC',
            800: 'DCCC',
            900: 'CM',
            1000: 'M',
            2000: 'MM',
            3000: 'MMM'
        }
        digits = [int(x) for x in format(num, '04d')]

        return ''.join(mapping[digits[i] * 10 ** (4 - i - 1)] for i in range(4))


if __name__ == '__main__':
    s = Solution()
    assert s.intToRoman(399) == 'CCCXCIX'
    assert s.intToRoman(1984) == 'MCMLXXXIV'
