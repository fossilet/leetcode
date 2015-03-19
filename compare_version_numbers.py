"""
https://leetcode.com/problems/compare-version-numbers/

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        rs1 = [int(s) for s in version1.split('.')]
        rs2 = [int(s) for s in version2.split('.')]
        l1, l2 = len(rs1), len(rs2)
        i = j = 0
        while i < l1 or j < l2:
            if rs1[i] == rs2[j]:
                if i != l1 - 1 and j != l2 - 1:
                    i += 1
                    j += 1
                    continue
                elif i == l1 - 1 and j != l2 - 1:
                    if any(x != 0 for x in rs2[j + 1:]):
                        return -1
                    else:
                        return 0
                elif i != l1 - 1 and j == l2 - 1:
                    if any(x != 0 for x in rs1[i + 1:]):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            elif rs1[i] > rs2[j]:
                return 1
            elif rs1[i] < rs2[j]:
                return -1
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    assert s.compareVersion('1', '0') == 1
    assert s.compareVersion('1.0', '1') == 0
    assert s.compareVersion('1.0.0', '1') == 0
    assert s.compareVersion('0.1', '0.0.1') == 1
    assert s.compareVersion('0.1.3', '0.1.3') == 0
    assert s.compareVersion('0.1.4', '0.1.3') == 1
    assert s.compareVersion('3', '3.1.4.1.5') == -1
    assert s.compareVersion('0.1', '1.1') == -1
    assert s.compareVersion('1.1', '1.2') == -1
    assert s.compareVersion('2.1', '1.10') == 1
