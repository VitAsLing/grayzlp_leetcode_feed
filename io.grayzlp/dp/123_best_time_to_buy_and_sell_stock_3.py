"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = hold2 = -sys.maxint - 1
        release1 = release2 = 0
        for i in prices:
            release2 = max(hold2 + i, release2)
            hold2 = max(release1 - i, hold2)
            release1 = max(hold1 + i, release1)
            hold1 = max(-i, hold1)
        return release2


# Test code
pri = [7, 2, 6, 3]
sol = Solution()
print sol.maxProfit(pri)
