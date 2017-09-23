"""
https://leetcode.com/problems/string-to-integer-atoi/description/

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

"""
import re
import sys


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        str = re.findall('^[+\-0]?\d*', str)

        try:
            res = int(''.join(str))
            MAX = 2**31 - 1
            MIN = - 2**31
            if res > MAX:
                return MAX
            elif res < MIN:
                return MIN
            return res
        except:
            return 0


# Test code
print Solution().myAtoi('+')
