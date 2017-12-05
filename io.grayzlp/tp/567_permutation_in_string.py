"""
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        board = {}
        for i in range(0, 26):
            ch = chr(i + ord('a'))
            board[ch] = 0
        for c in s1:
            board[c] += 1
        ok = 0
        for k, v in board.items():
            if v == 0:
                ok += 1

        i, j = 0, 0
        while j < len(s2):
            while j < len(s2) and not self.contain_all(board):
                board[s2[j]] -= 1
                if board[s2[j]] == 0:
                    ok += 1
                if board[s2[j]] == -1:
                    ok -= 1
                j += 1
                continue
            while i < j and ok != 26 and self.contain_all(board):
                board[s2[i]] += 1
                if board[s2[i]] == 0:
                    ok += 1
                if board[s2[i]] == 1:
                    ok -= 1
                i += 1
            if ok == 26:
                return True
        return False

    def contain_all(self, dic):
        for v in dic.values():
            if v > 0:
                return False
        return True


# Test code
print Solution().checkInclusion("caa", "aac")
