"""
https://leetcode.com/problems/restore-ip-addresses/description/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.backtracking(ans, [], s)
        return ans

    def backtracking(self, res, part, remain):
        if len(remain) > 12:
            return
        if len(part) == 4 and len(remain) == 0:
            res.append(".".join(part))
        else:
            i = 1
            while i < 4 and i <= len(remain):
                val = int(remain[0:i])
                if val < 256 and str(val) == remain[0:i]:
                    part.append(remain[0:i])
                    self.backtracking(res, part, remain[i:])
                    part.pop()
                i += 1


# Test code
print Solution().restoreIpAddresses("010010")
