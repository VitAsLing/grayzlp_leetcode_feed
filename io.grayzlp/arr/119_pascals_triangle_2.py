"""
https://leetcode.com/problems/pascals-triangle-ii/description/

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        cur = [1]
        for i in range(numRows):
            cur.append(1)
            for j in reversed(range(1, len(cur) - 1)):
                cur[j] = cur[j] + cur[j - 1]
        return cur
