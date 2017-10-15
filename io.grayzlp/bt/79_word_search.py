"""
https://leetcode.com/problems/word-search/description/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        used = [[False for i in range(0, len(board[0]))] for j in range(0, len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    if self.backtracking(board, used, i, j, word, 1):
                        return True
                    used[i][j] = False
        return False

    def backtracking(self, board, used, cur_x, cur_y, word, i):
        if i == len(word):
            return True
        else:
            for j in [-1, 0, 1]:
                if j in [- 1, 1]:
                    k_scope = [0]
                if j in [0]:
                    k_scope = [-1, 1]
                for k in k_scope:
                    next_x = cur_x + j
                    next_y = cur_y + k
                    if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                        if board[next_x][next_y] == word[i] and not used[next_x][next_y]:
                            used[next_x][next_y] = True
                            if self.backtracking(board, used, next_x, next_y, word, i + 1):
                                return True
                            used[next_x][next_y] = False

            return False


# Test code
sol = Solution()
b = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print sol.exist(b, 'ABCCED')
print sol.exist(b, 'SEE')
print sol.exist(b, 'ABCB')
