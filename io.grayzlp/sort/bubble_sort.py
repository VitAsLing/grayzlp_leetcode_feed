"""
Bubble Sort
"""
import random
import time


def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
    return nums


# Test code
length = 10000
arr = []
for k in range(length):
    arr.append(random.randint(1, length * 10))
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print (end_time - start_time) * 1000, "ms"
print arr

