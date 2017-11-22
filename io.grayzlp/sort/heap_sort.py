"""
Heap sort
"""

import random
import time


def heap_sort(nums):
    build_heap(nums)
    for i in reversed(range(1, len(nums))):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, i, 0)
    return nums


def build_heap(nums):
    size = len(nums)
    for i in reversed(range(0, size / 2)):
        max_heapify(nums, size, i)


def max_heapify(heap, size, index):
    left = (index << 1) + 1
    right = (index << 1) + 2
    largest = index
    if left < size and heap[left] > heap[largest]:
        largest = left
    if right < size and heap[right] > heap[largest]:
        largest = right
    if largest != index:
        heap[largest], heap[index] = heap[index], heap[largest]
        max_heapify(heap, size, largest)


# Test code
length = 1000000
arr = []
for k in range(length):
    arr.append(random.randint(1, length * 10))
start_time = time.time()
heap_sort(arr)
end_time = time.time()
print (end_time - start_time) * 1000, "ms"
print arr
