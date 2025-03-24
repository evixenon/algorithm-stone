#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 瞪眼法得 从左上(右下同理)开始, 小了往下, 大了往左, 该找到的就会找到
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n-1
        while True:
            cur = matrix[i][j]
            if cur == target:
                return True
            if cur > target:
                j -= 1
                if j < 0: # 越界
                    return False
            else:
                i += 1
                if i == m:
                    return False
            
# @lc code=end

