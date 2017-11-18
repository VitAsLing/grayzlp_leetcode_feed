"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            index = self.char_to_index(c)
            if not current.child[index]:
                current.child[index] = TrieNode()
            current = current.child[index]
        current.is_end_of_word = True

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(word, self.root)

    def search_helper(self, word, node):
        if len(word) == 0:
            if node.is_end_of_word:
                return True
            else:
                return False
        c = word[0]
        if c == '.':
            for child in node.child:
                if child and self.search_helper(word[1:], child):
                    return True
            return False
        else:
            index = self.char_to_index(c)
            if node.child[index] and self.search_helper(word[1:], node.child[index]):
                return True
            else:
                return False


class TrieNode(object):
    def __init__(self):
        self.child = [None] * 26
        self.is_end_of_word = False


# Test code
dic = WordDictionary()
dic.addWord("abc")
dic.addWord("aaa")
dic.addWord("ppp")
print dic.search('pp')
