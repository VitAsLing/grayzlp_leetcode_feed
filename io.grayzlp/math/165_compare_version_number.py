"""
https://leetcode.com/problems/compare-version-numbers/description/

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in (range(max(len(v1), len(v2)))):
            if i < len(v1):
                lhs = int(v1[i])
            else:
                lhs = 0
            if i < len(v2):
                rhs = int(v2[i])
            else:
                rhs = 0

            if lhs > rhs:
                return 1
            elif lhs < rhs:
                return -1
        return 0


print Solution().compareVersion('1.0', '1.0.2')
