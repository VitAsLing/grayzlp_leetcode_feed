"""
https://leetcode.com/problems/expression-add-operators/description/

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary
operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        self.backtracking(ans, "", num, target, 0, 0, 0)
        return ans

    def backtracking(self, res, part, num, target, pos, val, ratio):
        if pos == len(num):
            if val == target:
                res.append(part)
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            cur = int(num[pos:i + 1])
            cur_str = str(cur)

            if pos == 0:
                self.backtracking(res, part + cur_str, num, target, i + 1, cur, cur)
            else:
                self.backtracking(res, part + "+" + cur_str, num, target, i + 1, val + cur, cur)
                self.backtracking(res, part + "-" + cur_str, num, target, i + 1, val - cur, -cur)
                self.backtracking(res, part + "*" + cur_str, num, target, i + 1, val + ratio * (cur - 1), cur * ratio)


# Test code
print Solution().addOperators("105", 5)
