"""
https://leetcode.com/problems/permutation-sequence/description/

The set [1,2,3,...n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        re = [x for x in range(1, n + 1)]
        return self.helper(re, k - 1)

    def helper(self, remain, order):
        print remain, order
        l = len(remain)
        if l == 1:
            return str(remain[0])
        sel = order / self.factor(l - 1)
        next_order = order % self.factor(l - 1)
        cur = remain[sel]
        remain.remove(cur)
        left = self.helper(remain, next_order)
        return str(cur) + left

    def factor(self, a):
        if a == 1:
            return 1
        else:
            return a * self.factor(a - 1)


# Test code
print Solution().getPermutation(2, 2)

