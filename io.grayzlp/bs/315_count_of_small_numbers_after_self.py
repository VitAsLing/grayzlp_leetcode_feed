"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements
 to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        sorting = []
        for i in range(len(nums))[::-1]:
            num = nums[i]
            idx = self.bs(sorting, num)
            sorting.insert(idx, num)
            ans[i] = idx
        return ans

    def bs(self, arr, num):
        print num
        if not arr:
            return 0
        start = 0
        end = len(arr) - 1
        while 0 <= start <= end < len(arr):
            mid = (start + end) / 2
            if arr[mid] < num and (mid == (len(arr) - 1) or arr[mid + 1] >= num):
                return mid + 1
            elif mid == 0 and arr[0] >= num:
                return 0
            elif arr[mid] >= num:
                end = mid - 1
            elif arr[mid] < num:
                start = mid + 1


# Test code
print Solution().countSmaller([5, 4, 1, 2])
