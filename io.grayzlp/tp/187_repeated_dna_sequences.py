"""
https://leetcode.com/problems/repeated-dna-sequences/description/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying
DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        res = []
        for i in range(len(s) - 9):
            if s[i:i + 10] in dic:
                dic[s[i:i + 10]] += 1
            else:
                dic[s[i:i + 10]] = 1
        for k, v in dic.items():
            if v >= 2:
                res.append(k)
        return res


# Test code
print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
