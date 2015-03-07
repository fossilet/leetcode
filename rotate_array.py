"""
https://oj.leetcode.com/problems/rotate-array/

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = len(nums)
        if 0 < k:
            k %= l
            t = nums[-1:-1 - k:-1]
            for i in range(l - 1, k - 1, -1):
                nums[i] = nums[i - k]
            nums[0:k] = reversed(t)


if __name__ == '__main__':
    s = Solution()
    assert s.rotate([1], 0) == [1]
    assert s.rotate([0], 3) == [0]
    assert s.rotate([-1], 2) == [-1]
    assert s.rotate([1, 2], 1) == [2, 1]
    assert s.rotate([1, 2], 3) == [2, 1]
    assert s.rotate([0, 1], 2) == [0, 1]

    assert s.rotate([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert s.rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert s.rotate([3, 0, 1], 2) == [0, 1, 3]
    assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

    assert s.rotate([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
