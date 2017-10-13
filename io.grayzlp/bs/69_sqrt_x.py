"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        return self.sqrt_helper(x, 0, x)

    def sqrt_helper(self, target, lo, hi):
        if lo <= hi:
            mid = (lo + hi) / 2
            if mid * mid <= target < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > target:
                return self.sqrt_helper(target, lo, mid - 1)
            else:
                return self.sqrt_helper(target, mid + 1, hi)


# Test code
print Solution().mySqrt(6)
