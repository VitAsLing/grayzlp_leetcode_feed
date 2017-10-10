"""
https://leetcode.com/problems/merge-intervals/description/

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(lambda a, b: a.start - b.start)
        res = []
        start = intervals[0].start
        end = intervals[0].end
        for interval in intervals:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                res.append(Interval(start, end))
                start = interval.start
                end = interval.end
        res.append(Interval(start, end))
        return res


# Test code
res = Solution().merge([Interval(1, 4), Interval(4, 5)])
for i in res:
    print i.start, i.end
