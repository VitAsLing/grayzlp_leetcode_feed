"""
https://leetcode.com/problems/combination-sum-iii/description/

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]


"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.back_tracking(ans, [], 1, k, n)
        return ans

    def back_tracking(self, res, part, mi, left, remain):
        if left * mi > remain or left * 9 < remain:
            return
        if left == 1:
            if remain <= 9:
                part.append(remain)
                res.append(list(part))
                part.pop()
            return

        for i in range(mi, 10):
            part.append(i)
            self.back_tracking(res, part, i + 1, left - 1, remain - i)
            part.pop()


# Test code
print Solution().combinationSum3(3, 10)
