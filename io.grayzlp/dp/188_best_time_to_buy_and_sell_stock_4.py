"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices) / 2:
            return self.quick(prices)
        if len(prices) < 2:
            return 0
        dp = [[0 for i in range(len(prices))] for j in range(k + 1)]
        for i in range(1, k + 1):
            tmp_max = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], tmp_max + prices[j])
                tmp_max = max(tmp_max, dp[i - 1][j - 1] - prices[j])
        return dp[k][len(prices) - 1]

    def quick(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# Test code
print Solution().maxProfit(5, [5, 1, 4, 9, 1, 2])
