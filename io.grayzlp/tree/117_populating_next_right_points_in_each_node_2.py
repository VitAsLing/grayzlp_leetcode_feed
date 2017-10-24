"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur = root
        head = None
        prev = None
        while cur:
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head
            head = None
            prev = None

    # @param root, a tree link node
    # @return nothing
    def connect2(self, root):
        par = root
        while par:
            cur = par
            prev = None
            while cur:
                if not cur.left and not cur.right:
                    cur = cur.next
                    continue
                elif cur.left and cur.right:
                    if prev:
                        prev.next = cur.left
                    cur.left.next = cur.right
                    prev = cur.right
                else:
                    single = cur.left
                    if not single:
                        single = cur.right
                    if prev:
                        prev.next = single
                    prev = single
                cur = cur.next
            if par.left:
                par = par.left
            elif par.right:
                par = par.right
            else:
                par = par.next


# Test code
tln1 = TreeLinkNode(1)
tln2 = TreeLinkNode(2)
tln3 = TreeLinkNode(3)
tln4 = TreeLinkNode(4)
tln5 = TreeLinkNode(5)
tln1.left = tln2
tln2.left = tln4
tln1.right = tln3
tln3.right = tln5
Solution().connect(tln1)
print tln1.left.left.next.val
