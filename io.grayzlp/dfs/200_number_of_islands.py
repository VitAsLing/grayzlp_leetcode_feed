"""
https://leetcode.com/problems/number-of-islands/description/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0

        count = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == '1':
                    count += 1
                    self.extend(grid, i, j)
        return count

    def extend(self, grid, i, j):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or
                grid[i][j] != '1'):
            return
        grid[i][j] = '0'
        self.extend(grid, i - 1, j)
        self.extend(grid, i, j - 1)
        self.extend(grid, i + 1, j)
        self.extend(grid, i, j + 1)


# Test code
case = [['1', '1', '1'],
        ['0', '1', '0'],
        ['1', '0', '1'],
        ['1', '1', '1']]

print Solution().numIslands(case)
