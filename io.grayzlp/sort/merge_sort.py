"""
Merge sort
"""
import random
import time
from collections import deque


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] < right[0] else right.popleft())
        merged.extend(left if left else right)
        return list(merged)

    mid = int(len(nums) // 2)
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


# Test code
length = 1000000
arr = []
for k in range(length):
    arr.append(random.randint(1, length * 10))
start_time = time.time()
arr = merge_sort(arr)
end_time = time.time()
print (end_time - start_time) * 1000, "ms"
# print arr
