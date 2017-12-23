"""
https://leetcode.com/problems/find-median-from-data-stream/description/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no
middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
from heapq import *


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(small) > len(large):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(small) == len(large):
            return (large[0] - small[0]) / 2.0
        else:
            return large[0]


# Test code
obj = MedianFinder()
obj.addNum(1)
print obj.findMedian()
obj.addNum(2)
print obj.findMedian()
obj.addNum(3)
print obj.findMedian()
