"""
https://leetcode.com/problems/candy/description/

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1 for x in range(0, len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1
        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i]:
                candy[i - 1] = max(candy[i - 1], candy[i] + 1)

        ans = 0
        for i in range(0, len(candy)):
            ans += candy[i]
        return ans


# Test code
print Solution().candy([4, 3, 2, 3])
