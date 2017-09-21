"""
17. Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                 '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(kvmap.get(digits))
        first = kvmap.get(digits[0])
        other = self.letterCombinations(digits[1:])
        return [f + o for f in first for o in other]


# Test code
print Solution().letterCombinations('234')

