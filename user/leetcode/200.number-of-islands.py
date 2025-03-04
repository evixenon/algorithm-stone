# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def dfs(self, r, c, grid):
        # 先污染后治理 判断代码
        if r >= len(grid) or c >= len(grid[0])\
        or r < 0 or c < 0: return
        
        if grid[r][c] == "0": return
        # 标记法, 所以遍历到的点标 "0"
        grid[r][c] = "0"
        self.dfs(r+1, c, grid)
        self.dfs(r, c+1, grid)
        self.dfs(r-1, c, grid)
        self.dfs(r, c-1, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        count =  0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    count += 1
                    self.dfs(r, c, grid)
        
        return count
        
# @lc code=end

