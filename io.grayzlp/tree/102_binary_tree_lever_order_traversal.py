"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Iteratively
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que = [root]
        ans = []
        while len(que):
            remain_count = len(que)
            cur_res = []
            while remain_count > 0:
                remain_count -= 1
                node = que.pop()
                if node.left:
                    que.insert(0, node.left)
                if node.right:
                    que.insert(0, node.right)
                cur_res.append(node.val)
            ans.append(cur_res)
        return ans

    # Recursively
    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        self.levelOrderHelp(ans, [root])
        return ans

    def levelOrderHelp(self, res, cur):
        if not len(cur):
            return
        next = []
        tmp = []
        for node in cur:
            tmp.append(node.val)
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
        res.append(tmp)
        self.levelOrderHelp(res, next)


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(2)
n5 = TreeNode(3)
n1.left = n2
n2.left = n3
n1.right = n4
n4.right = n5
print Solution().levelOrder(n1)
