"""
https://leetcode.com/problems/maximum-product-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_p = nums[0]
        min_p = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if max_p == 0:
                max_p = num
                min_p = num
                best = max(max_p, best)
                continue

            if num == 0:
                max_p = 0
                min_p = 0
                best = max(best, max_p)
            elif num < 0:
                max_p, min_p = max(min_p * num, num), min(max_p * num, num)
                best = max(best, max_p)
            else:
                max_p, min_p = max(max_p * num, num), min(min_p * num, num)
                best = max(best, max_p)
        return best


# Test code
print Solution().maxProduct([0, 3, 2, -1, -3, 4, -3, -1])
