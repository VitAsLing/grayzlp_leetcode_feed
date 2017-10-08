"""
https://leetcode.com/problems/permutations/description/


Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(res, [], nums)
        return res

    def backtracking(self, res, temp_list, nums):
        if len(temp_list) == len(nums):
            res.append(list(temp_list))
        else:
            for num in nums:
                if num in temp_list:
                    continue
                temp_list.append(num)
                self.backtracking(res, temp_list, nums)
                temp_list.remove(num)


# Test code
print Solution().permute([1, 2])
