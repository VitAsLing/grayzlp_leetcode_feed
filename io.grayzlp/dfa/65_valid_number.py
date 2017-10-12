"""
https://leetcode.com/problems/valid-number/description/

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        states = [{},
                  # 1 initial
                  {'blank': 1, 'sign': 2, 'digital': 3, '.': 4},
                  # 2 after a sign
                  {'digital': 3, '.': 4},
                  # 3 after some digital
                  {'digital': 3, '.': 5, 'e': 6, 'blank': 9},
                  # 4 after a point
                  {'digital': 5},
                  # 5 after a point and some digital
                  {'digital': 5, 'e': 6, 'blank': 9},
                  # 6 after e
                  {'digital': 8, 'sign': 7},
                  # 7 after e and a sign
                  {'digital': 8},
                  # 8 after e and some digital
                  {'digital': 8, 'blank': 9},
                  # 9 tail blank
                  {'blank': 9}
                  ]
        current_state = 1
        for c in s:
            if '9' >= c >= '0':
                c = 'digital'
            elif c == '+' or c == '-':
                c = 'sign'
            elif c == ' ':
                c = 'blank'
            if c not in states[current_state].keys():
                return False
            current_state = states[current_state][c]
        if current_state not in [3, 5, 8, 9]:
            return False
        return True


# Test code
print Solution().isNumber("2e0")
