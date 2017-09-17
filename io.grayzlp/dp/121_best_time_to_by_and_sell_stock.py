"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Can improve with O(1) space
        dp = [0 for x in range(len(prices))]
        max_profit = 0
        for i in range(1, len(prices)):
            dp[i] = max(0, dp[i - 1] + prices[i] - prices[i - 1])
            max_profit = max(max_profit, dp[i])
        return max_profit


# Test code
sol = Solution()
p = [7, 1, 5, 3, 6, 4]
print sol.maxProfit(p)

