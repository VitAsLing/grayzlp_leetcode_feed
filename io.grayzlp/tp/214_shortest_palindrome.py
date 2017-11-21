"""
https://leetcode.com/problems/shortest-palindrome/description/

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""


class Solution(object):
    # solution base kmp
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        trick = s + '#' + s[::-1]
        print trick
        lps = self.build_lps(trick)

        print lps
        return s[lps[len(lps) - 1]:][::-1] + s

    def build_lps(self, p):
        lps = [0 for i in range(len(p))]
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def shortestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(0, len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    # my solution tle
    def shortestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        for i in reversed(range(0, len(s))):
            j, k = 0, i
            conform = True
            while j < k:
                if s[j] != s[k]:
                    conform = False
                    break
                else:
                    j += 1
                    k -= 1
            if conform:
                res = ''
                for z in reversed(range(i + 1, len(s))):
                    res += s[z]
                res += s
                return res


# Test code
print Solution().shortestPalindrome("aacecaaa")
