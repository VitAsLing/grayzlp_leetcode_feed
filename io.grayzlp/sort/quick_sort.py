"""
Quick sort
"""
import random
import time
from collections import deque


def quick_sort(nums):
    return quick_sort_helper(nums, 0, len(nums))


def quick_sort_helper(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        quick_sort_helper(nums, lo, p)
        quick_sort_helper(nums, p + 1, hi)
    return nums


def partition(nums, lo, hi):
    pivot = nums[hi - 1]
    i = lo - 1
    for j in range(lo, hi):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    if nums[hi - 1] < nums[i + 1]:
        nums[hi - 1], nums[i + 1] = nums[i + 1], nums[hi - 1]
    return i + 1


# Test code
length = 1000000
arr = []
for k in range(length):
    arr.append(random.randint(1, length * 10))
start_time = time.time()
arr = quick_sort(arr)
end_time = time.time()
print (end_time - start_time) * 1000, "ms"
print arr
