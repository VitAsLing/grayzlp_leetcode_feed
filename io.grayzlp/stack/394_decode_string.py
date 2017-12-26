"""
https://leetcode.com/problems/decode-string/description/

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is
being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur = ''
        multiples = ''
        for c in s:
            if c == '[':
                stack.append((cur, multiples))
                cur = ''
                multiples = ''
            if c.isdigit():
                multiples += c
            if c.isalpha():
                cur += c
            if c == ']':
                prev, pre_m = stack.pop()
                print prev, pre_m
                for i in range(int(pre_m)):
                    prev += cur

                cur = prev
                multiples = ''
        return cur


# Test code
print Solution().decodeString("2[f2[e]g]")
