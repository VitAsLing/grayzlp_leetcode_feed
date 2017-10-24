"""
https://leetcode.com/problems/pascals-triangle/description/

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        cur = [1]
        for i in range(numRows):
            ans.append(list(cur))
            cur.append(1)
            for j in reversed(range(1, len(cur) - 1)):
                cur[j] = cur[j] + cur[j - 1]
        return ans


# Test code
print Solution().generate(0)
