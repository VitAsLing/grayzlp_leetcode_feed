"""
https://leetcode.com/problems/h-index-ii/description/

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

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
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) >> 1
            if citations[mid] == (length - mid):
                return citations[mid]
            if citations[mid] > (length - mid):
                right = mid - 1
            else:
                left = mid + 1
        return length - (right + 1)


# Test code
print Solution().hIndex([0, 0, 3, 5, 6])
