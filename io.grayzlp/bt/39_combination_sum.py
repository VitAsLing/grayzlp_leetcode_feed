"""
https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


# Another solution
class Solution2(object):
    def combinationSum(self, candidates, target):
        ret = []
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
                temp_li.append(candidates[i])
                self.backtracing(li_li, temp_li, candidates, remain - candidates[i], i)
                temp_li.pop()


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.helper(candidates, 0, target)

    def helper(self, candidates, start, target):
        n = len(candidates)
        ret = []
        if start == n:
            return ret
        elif start == n - 1:

            item = candidates[start]
            count = 0
            s = item * count
            while s <= target:
                if s == target:
                    ret.append([item] * count)
                count += 1
                s = item * count
        else:
            item = candidates[start]
            count = 0
            s = item * count
            while s <= target:
                next_ret = self.helper(candidates, start + 1, target - s)
                for li in next_ret:
                    ret.append([item] * count + li)
                count += 1
                s = item * count
        return ret


# Test code
print Solution2().combinationSum([2, 3, 6, 7], 7)
