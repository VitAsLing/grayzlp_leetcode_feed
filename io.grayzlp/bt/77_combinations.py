"""
https://leetcode.com/problems/combinations/description/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(res, [], 1, n - k + 1, k)
        return res

    def backtracking(self, res, tmp, start, end, remain):
        if remain == 0:
            res.append(list(tmp))
        else:
            for i in range(start, end + 1):
                tmp.append(i)
                self.backtracking(res, tmp, i + 1, end + 1, remain - 1)
                tmp.remove(i)


# Test code
print Solution().combine(20, 16)
