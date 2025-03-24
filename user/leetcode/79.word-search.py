# @before-stub-for-debug-begin
from python3problem79 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):
            if k == len(word): # 找到
                return True
            if i < 0 or j < 0 or i > m-1 or j > n-1: # 超出边界
                return False
            # if not board[i][j]: # 选过了
            #     return False
            
            target = word[k]
            if board[i][j] != target: # 不对
                return False
            
            board[i][j] = ""
            left = dfs(i, j-1, k+1)
            right = dfs(i, j+1, k+1)
            up = dfs(i-1, j, k+1)
            down = dfs(i+1, j, k+1)
            board[i][j] = target # 恢复现场
            return left or right or up or down
        
        found = 0
        for i in range(m):
            for j in range(n):
                found = dfs(i, j, 0)
                if found:
                    return True
        return False
# @lc code=end

