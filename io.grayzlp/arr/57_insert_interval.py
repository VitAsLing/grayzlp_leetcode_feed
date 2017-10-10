"""
https://leetcode.com/problems/insert-interval/description/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        n = len(intervals)
        res = []
        while i < n:
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
                i += 1
            else:
                break
        while i < n:
            if intervals[i].start <= newInterval.end:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                i += 1
            else:
                break
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


res = Solution().insert([Interval(1, 3), Interval(7, 9)], Interval(4, 5))
for i in res:
    print i.start, i.end
