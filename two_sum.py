#! /usr/bin/env python3
"""
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

Since 4/3/20    14 15:39
"""


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        length = len(num)
        for i in range(length):
            for j in range(i + 1, length):
                if num[i] + num[j] == target:
                    return i + 1, j + 1

    def main(self):
        assert self.twoSum([2, 7, 11, 15], 9) == (1, 2)


if __name__ == '__main__':
    Solution().main()
