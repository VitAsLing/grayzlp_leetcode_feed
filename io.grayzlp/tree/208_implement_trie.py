"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""


class TreeNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            idx = self.char_to_index(c)
            if not current.children[idx]:
                current.children[idx] = TreeNode()
            current = current.children[idx]
        current.is_end_of_word = True

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            idx = self.char_to_index(c)
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return current and current.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            idx = self.char_to_index(c)
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return current is not None


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print obj.search("word")
print obj.startsWith("wo")
print obj.startsWith('words')
