"""
https://leetcode.com/problems/the-skyline-problem/description/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a
distance.
 Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A),
 write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the
x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed
that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles
 grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10],
[19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that
uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point,
where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8],
[24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5],
[7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output
as such: [...[2 3], [4 5], [12 7], ...]


"""
from heapq import heappop, heappush, nsmallest, heapify


class PriorityQueue(object):
    # customize a maximum priority queue
    def __init__(self):
        self._queue = []

    def put(self, item):
        heappush(self._queue, (-item, item))

    def get(self):
        return heappop(self._queue)[-1]

    def peek(self):
        return nsmallest(1, self._queue)[-1]

    def remove(self, item):
        for el in self._queue:
            if el[-1] == item:
                self._queue.remove(el)
                break
        heapify(self._queue)


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []
        res = []
        prev_end = 0
        prev_height = -1
        for b in buildings:
            if b[1] <= prev_end and b[2] <= prev_height:
                continue
            else:
                height.append([b[0], -b[2]])
                height.append([b[1], b[2]])
                prev_end = b[1]
                prev_height = b[2]

        def sort_method(x, y):
            if x[0] != y[0]:
                return x[0] - y[0]
            return x[1] - y[1]

        height.sort(sort_method)
        queue = PriorityQueue()
        queue.put(0)
        prev = 0
        for h in height:
            if h[1] < 0:
                queue.put(-h[1])
            else:
                queue.remove(h[1])

            cur = queue.peek()
            if prev != cur:
                res.append([h[0], cur[-1]])
                prev = cur
        return res


# Test code
bu= [[1, 2, 1], [2, 3, 2]]
print Solution().getSkyline(bu)
