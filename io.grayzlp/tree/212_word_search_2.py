"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""
import time


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.build_trie(words)

        row = len(board)
        col = len(board[0])
        ans = []
        for i in range(row):
            for j in range(col):
                self.dfs(board, i, j, root, ans)
        return ans

    def build_trie(self, words):
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                index = self.char2index(c)
                if not cur.child[index]:
                    cur.child[index] = TrieNode()
                cur = cur.child[index]
            cur.word = w
        return root

    def char2index(self, c):
        return ord(c) - ord('a')

    def dfs(self, board, x, y, node, res):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == '#':
            return
        c = board[x][y]
        index = self.char2index(c)
        if not node.child[index]:
            return

        node = node.child[index]
        if node.word:
            res.append(node.word)
            node.word = None
        board[x][y] = '#'
        self.dfs(board, x + 1, y, node, res)
        self.dfs(board, x - 1, y, node, res)
        self.dfs(board, x, y + 1, node, res)
        self.dfs(board, x, y - 1, node, res)
        board[x][y] = c


class TrieNode(object):
    def __init__(self):
        self.child = [None] * 26
        self.word = None


# Test code
p = [["b", "a", "a", "b", "a", "b"],
     ["a", "b", "a", "a", "a", "a"],
     ["a", "b", "a", "a", "a", "b"],
     ["a", "b", "a", "b", "b", "a"],
     ["a", "a", "b", "b", "a", "b"],
     ["a", "a", "b", "b", "b", "a"],
     ["a", "a", "b", "a", "a", "b"]]
words = ["aab", "bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
         "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
         "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
         "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
         "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
         "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
         "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
         "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
         "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
         "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]

start = time.time()
print Solution().findWords(p, words)
end = time.time()
print end - start
