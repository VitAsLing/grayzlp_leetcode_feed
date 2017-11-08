"""
https://leetcode.com/problems/happy-number/description/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process
ends in 1 are happy numbers.

Example: 19 is a happy number

(1)2 + (9)2 = 82
(8)2 + (2)2 = 68
(8)2 + (6)2 = 100
(1)2 + (0)2 + (0)2 = 1

"""


class Solution(object):
    def isHappy(self, n):
        slow = fast = n
        while True:
            slow = self.dightSquareSum(slow)
            fast = self.dightSquareSum(fast)
            fast = self.dightSquareSum(fast)
            if slow == fast:
                break
        return slow == 1

    def dightSquareSum(self, num):
        res = 0
        while num:
            res += (num % 10) * (num % 10)
            num /= 10
        return res

    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        appear = []
        while n != 1 and n not in appear:
            appear.append(n)
            n = self.get_sum_of_squares_of_digits(n)
        return n == 1

    def get_sum_of_squares_of_digits(self, num):
        res = 0
        num_str = str(num)
        for c in num_str:
            res += int(c) * int(c)
        return res


# Test code
print Solution().isHappy(18)
