"""
https://leetcode.com/problems/create-maximum-number/description/

Given two arrays of length m and n with digits 0-9 representing two numbers.
 Create the maximum number of length k <= m + n from digits of the two. The
 relative order of the digits from the same array must be preserved. Return
 an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

"""


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        ans = [0 for _ in xrange(k)]
        for i in range(max(0, k - m), min(k, n) + 1):
            candidate = self.merge(self.maxArray(nums1, i), self.maxArray(nums2, k - i), k)
            if self.compare(candidate, 0, ans, 0):
                ans = candidate
        return ans

    def maxArray(self, arr, count):
        ans = [0 for _ in xrange(count)]
        n = len(arr)
        j = 0
        for i in xrange(len(arr)):
            while n - i + j > count and j > 0 and ans[j - 1] < arr[i]:
                j -= 1
            if j < count:
                ans[j] = arr[i]
                j += 1
        return ans

    def merge(self, lhs, rhs, count):
        ans = [0 for _ in xrange(count)]
        i = 0
        j = 0
        for r in xrange(count):
            if self.compare(lhs, i, rhs, j):
                ans[r] = lhs[i]
                i += 1
            else:
                ans[r] = rhs[j]
                j += 1
        return ans

    def compare(self, arr1, i, arr2, j):
        while i < len(arr1) and j < len(arr2) and arr1[i] == arr2[j]:
            i += 1
            j += 1
        return j == len(arr2) or (i < len(arr1) and arr1[i] > arr2[j])


# Test code
print(Solution().maxNumber([1, 3, 4], [9, 8], 4))
