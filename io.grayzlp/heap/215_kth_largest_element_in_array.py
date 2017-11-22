"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.

"""
import sys


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-sys.maxint + 1 for i in range(k)]
        for num in nums:
            if num > heap[0]:
                heap[0] = num
                self.max_heapify(heap, 0)
        return heap[0]

    def max_heapify(self, heap, index):
        left = (index << 1) + 1
        right = (index << 1) + 2
        minimal = index
        if left < len(heap) and heap[left] < heap[minimal]:
            minimal = left
        if right < len(heap) and heap[right] < heap[minimal]:
            minimal = right
        if minimal != index:
            heap[minimal], heap[index] = heap[index], heap[minimal]
            self.max_heapify(heap, minimal)


# Test code
print Solution().findKthLargest([1, 3, 4, 6, 2, 6], 5)
