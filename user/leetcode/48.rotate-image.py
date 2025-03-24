# @before-stub-for-debug-begin
from python3problem48 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 不对, 不能用另一个矩阵
        # 那就四个一组转, 转左上四分之一方块
        # n 单数怎么办: 行或列少一
        n = len(matrix)
        
        for i in range(n//2):
            for j in range((n+1)//2):
                tmp = matrix[i][j]
                matrix[i][j]= matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = tmp
        
# @lc code=end

