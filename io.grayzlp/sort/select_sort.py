"""
Select Sort
"""
import random
import time


def select_sort(nums):
    for i in range(0, len(nums) - 1):
        index_of_min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index_of_min]:
                index_of_min = j
        if index_of_min != i:
            nums[i], nums[index_of_min] = nums[index_of_min], nums[i]


# Test code
length = 10000
arr = []
for k in range(length):
    arr.append(random.randint(1, length * 10))
start_time = time.time()
select_sort(arr)
end_time = time.time()
print (end_time - start_time) * 1000, "ms"
print arr

