"""
https://leetcode.com/problems/binary-search-tree-iterator/description/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.items = self.inorder(root)
        self.offset = -1

    def inorder(self, node):
        stack = []
        ans = []
        cur = node
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.offset + 1 < len(self.items)

    def next(self):
        """
        :rtype: int
        """
        self.offset += 1
        return self.items[self.offset]


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n2.left = n1
n2.right = n3

i, v = BSTIterator(n2), []
while i.hasNext():
    v.append(i.next())
print v
