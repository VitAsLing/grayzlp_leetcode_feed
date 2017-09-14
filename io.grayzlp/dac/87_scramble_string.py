"""
https://leetcode.com/problems/scramble-string/description/

"""


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        size = len(s1)
        c_map = [0 for i in range(0, 256)]
        for i in range(size):
            c_map[ord(s1[i])] += 1
            c_map[ord(s2[i])] -= 1
        for i in range(0, 256):
            if c_map[i] != 0:
                return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[0:i], s2[(size - i):size]) and self.isScramble(s1[i:], s2[0: (size - i)]):
                return True
        return False


# Test code
sol = Solution()
print sol.isScramble("abb", "bba")
