"""
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        candidates = sorted(candidates)
        self.backtracing(ret, [], candidates, target, 0)
        return ret

    def backtracing(self, li_li, temp_li, candidates, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            # add the copy of temp list
            li_li.append(list(temp_li))
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                temp_li.append(candidates[i])
                self.backtracing(li_li, temp_li, candidates, remain - candidates[i], i + 1)
                temp_li.pop()


# Test code
print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
