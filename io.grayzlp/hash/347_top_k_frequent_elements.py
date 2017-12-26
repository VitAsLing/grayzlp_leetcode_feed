"""
https://leetcode.com/problems/top-k-frequent-elements/description/

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in range(len(nums) + 1)]
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for i in dic.keys():
            bucket[dic[i]].append(i)
        print dic, bucket
        res = []
        pos = len(nums)
        while pos >= 0 and len(res) < k:
            res = res + bucket[pos]
            pos -= 1
        return res


# Test code
print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
