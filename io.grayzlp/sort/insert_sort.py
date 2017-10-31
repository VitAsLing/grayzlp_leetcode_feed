"""
Insert Sort
"""
import random
import time


def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp


# Test code
length = 10000
arr = []
for k in range(length):
    arr.append(random.randint(1, length * 10))
start_time = time.time()
insert_sort(arr)
end_time = time.time()
print (end_time - start_time) * 1000, "ms"
print arr
