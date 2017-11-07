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


# Define UF Structure
class UF(object):
    def __init__(self, m, n, grid):
        self.count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    self.count += 1
        self.id = [i for i in range(0, m * n)]
        self.group_size = [1 for i in range(0, m * n)]

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        gp = self.find(p)
        gq = self.find(q)
        if gp == gq:
            return
        if self.group_size[gp] < self.group_size[gq]:
            self.id[gp] = gq
            self.group_size[gq] += self.group_size[gp]
        else:
            self.id[gq] = gp
            self.group_size[gp] += self.group_size[gq]
        self.count -= 1

    def connect(self, p, q):
        if self.find(p) == self.find(q):
            return True
        else:
            return False


class Solution(object):
    # Union Find
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        uf = UF(m, n, grid)
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '0':
                    continue
                p = i * n + j
                if i + 1 < m:
                    if grid[i + 1][j] == '1':
                        uf.union(p, p + n)
                if j + 1 < n:
                    if grid[i][j + 1] == '1':
                        uf.union(p, p + 1)
        print uf.id
        return uf.count

    # DFS Solution
    def numIslands2(self, grid):
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
        ['0', '1', '1'],
        ['1', '0', '1'],
        ['0', '1', '1']]

print Solution().numIslands(case)
