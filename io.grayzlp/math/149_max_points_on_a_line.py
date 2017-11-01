"""
https://leetcode.com/problems/max-points-on-a-line/description/

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def get_gcd(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return get_gcd(rhs, lhs % rhs)


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)
        res = 0
        map = {}
        for i in range(len(points)):
            map.clear()
            overlap = 0
            best = 0
            for j in range(i + 1, len(points)):
                delta_x = points[j].x - points[i].x
                delta_y = points[j].y - points[i].y

                if delta_x == 0 and delta_y == 0:
                    overlap += 1
                    continue

                gcd = get_gcd(delta_x, delta_y)
                delta_x /= gcd
                delta_y /= gcd

                if delta_x in map.keys():
                    if delta_y in map[delta_x].keys():
                        map[delta_x][delta_y] += 1
                    else:
                        map[delta_x][delta_y] = 1
                else:
                    map[delta_x] = {}
                    map[delta_x][delta_y] = 1
                best = max(best, map[delta_x][delta_y])
            res = max(res, best + overlap + 1)
        return res


# Test code
p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(3, 6)
p4 = Point(0, 1)
print Solution().maxPoints([p1, p2, p3, p4])
