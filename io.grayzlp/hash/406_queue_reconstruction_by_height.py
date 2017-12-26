"""
https://leetcode.com/problems/queue-reconstruction-by-height/description/

Suppose you have a random list of people standing in a queue. Each person is described
 by a pair of integers (h, k), where h is the height of the person and k is the number
 of people in front of this person who have a height greater than or equal to h. Write
 an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        dic, height, ans = {}, [], []
        for i in xrange(len(people)):
            p = people[i]
            if p[0] in dic:
                dic[p[0]].append((p[1], i))
            else:
                dic[p[0]] = [(p[1], i)]
                height.append(p[0])
        height.sort()
        for h in height[::-1]:
            dic[h].sort()
            for p in dic[h]:
                ans.insert(p[0], people[p[1]])
        return ans


# Test code
print Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
