"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""
from collections import defaultdict


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = defaultdict(lambda: [])
        labels = {}
        if not head:
            return None
        sentinel = RandomListNode(-1)
        prev = sentinel
        cur = head
        while cur is not None:
            copy = RandomListNode(cur.label)
            labels[cur.label] = copy
            prev.next = copy
            if cur.random:
                dic[cur.random.label].append(copy)
            prev = copy
            cur = cur.next
        for k, v in dic.iteritems():
            for node in v:
                node.random = labels[k]
        return sentinel.next


# Test code
n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n1.random = n4
res = Solution().copyRandomList(n1)
print res.random.label
