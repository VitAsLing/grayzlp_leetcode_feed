"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3  1,3,2
3,2,1  1,2,3
1,1,5  1,5,1

"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i == 0:
            self.reverseSort(nums, 0, n - 1)
            return
        else:
            val = nums[i - 1]
            j = n - 1
            while j >= i:
                if nums[j] > val:
                    break
                j -= 1
            self.swap(nums, j,  i - 1)
            self.reverseSort(nums, i, n - 1)
            return

    def reverseSort(self, nums, start, end):
        if start > end:
            return
        for i in range(start, ((start + end) / 2) + 1):
            self.swap(nums, i, start + end - i)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


# Test code
n = [9, 5, 2, 5, 3, 1]
Solution().nextPermutation(n)
print n
