"""
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns the number of 1 bits it has (also known as the Hamming
weight). For example, the 32-bit integer 11 has binary representation 00000000000000000000000000001011, so the
function should
return 3.

"""


class Solution(object):
    def hammingWeight(self, num):
        res = 0
        for i in range(0, 31):
            res += num & 1
            num >>= 1
        res += num
        return res


# Test code
print Solution().hammingWeight(15)
