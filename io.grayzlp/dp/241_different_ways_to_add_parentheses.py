"""
https://leetcode.com/problems/different-ways-to-add-parentheses/description/

Given a string of numbers and operators, return all possible results from computing all the different possible
 ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.withdp(input, {})

    def withdp(self, input, dp):
        if input in dp:
            return dp[input]
        res = []
        for i in range(len(input)):
            c = input[i]
            if c in ['*', '+', '-']:
                left = self.withdp(input[0:i], dp)
                right = self.withdp(input[i + 1:], dp)
                for m in left:
                    for n in right:
                        if c == '+':
                            res.append(m + n)
                        if c == '-':
                            res.append(m - n)
                        if c == '*':
                            res.append(m * n)
        if not len(res):
            res.append(int(input))
        dp[input] = res
        return res


# Test code
print Solution().diffWaysToCompute("2 - 1 - 1")
