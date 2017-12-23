"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not
necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize
algorithms should be stateless.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    NN = "X"
    SPLIT = ","

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        self.build_str(root, data)
        return Codec.SPLIT.join(data)

    def build_str(self, root, res):
        if not root:
            res.append(Codec.NN)
        else:
            res.append(str(root.val))
            self.build_str(root.left, res)
            self.build_str(root.right, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(Codec.SPLIT)
        return self.build_tree(arr)

    def build_tree(self, arr):
        cur = arr.pop(0)
        if cur == Codec.NN:
            return None
        else:
            node = TreeNode(int(cur))
            node.left = self.build_tree(arr)
            node.right = self.build_tree(arr)
            return node


# Test code
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)


def print_tree(node):
    print node.val
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


t1.left = t2
t1.right = t3
print Codec().serialize(t1)
print_tree(Codec().deserialize(Codec().serialize(t1)))
