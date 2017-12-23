"""
https://leetcode.com/problems/h-index/description/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute
the researcher's h - index.

According to the definition of h - index on Wikipedia: "A scientist has index h if h of his/her N papers have at least
h citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them
had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each
and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        if length == 0:
            return 0
        idx = [0] * (length + 1)
        for i in range(length):
            if citations[i] > length:
                idx[length] += 1
            else:
                idx[citations[i]] += 1

        res = 0
        for i in reversed(range(0, length + 1)):
            res += idx[i]
            if res >= i:
                return i
        return 0


# Test code
print Solution().hIndex([3, 0, 1, 5, 6])
