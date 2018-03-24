"""
https://leetcode.com/problems/additive-number/description/

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers,
each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

"""


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, (len(num) / 2) + 1):
            if num[0] == '0' and i > 1:
                break
            x1 = int(num[0:i])
            j = 1
            while len(num) - i - j >= max(i, j):
                if num[i] == '0' and j > 1:
                    break
                x2 = int(num[i:i + j])
                if self.isValid(x1, x2, i + j, num):
                    return True
                j += 1
        return False

    def isValid(self, first, second, start, num):
        print first, second, start, num
        if start == len(num):
            return True
        second = first + second
        first = second - first
        return num[start:].startswith(str(second)) and self.isValid(first, second, start + len(str(second)), num)


# Test code
print(Solution().isAdditiveNumber("1232447"))
