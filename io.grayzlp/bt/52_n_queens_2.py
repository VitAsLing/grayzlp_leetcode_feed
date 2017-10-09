"""
https://leetcode.com/problems/n-queens-ii/description/

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

"""


class Solution(object):
    def __init__(self):
        self.count = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col_rec = [False] * n
        d_rec = [False] * 2 * n
        rec_d_rec = [False] * 2 * n
        self.backtracking(0, col_rec, d_rec, rec_d_rec, n)
        return self.count

    def backtracking(self, row, col_rec, d_rec, rev_d_rec, n):
        if row == n:
            self.count += 1
        else:
            for col in range(0, n):
                idx1 = col + row
                idx2 = col - row + n
                if col_rec[col] or d_rec[idx1] or rev_d_rec[idx2]:
                    continue
                else:
                    col_rec[col] = True
                    d_rec[idx1] = True
                    rev_d_rec[idx2] = True
                    self.backtracking(row + 1, col_rec, d_rec, rev_d_rec, n)
                    col_rec[col] = False
                    d_rec[idx1] = False
                    rev_d_rec[idx2] = False


# Test code
print Solution().totalNQueens(8)
