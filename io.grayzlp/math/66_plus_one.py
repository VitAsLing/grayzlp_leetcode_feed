"""
https://leetcode.com/problems/plus-one/description/

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        completed = False
        while i >= 0 and not completed:
            cur = digits[i]
            s = cur + 1
            if s == 10:
                digits[i] = 0
                i -= 1
            else:
                digits[i] = s
                completed = True

        if i == -1 and not completed:
            digits.insert(0, 1)
        return digits


# Test code
print Solution().plusOne([1, 0, 1])

