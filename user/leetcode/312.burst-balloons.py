# @before-stub-for-debug-begin
from python3problem312 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 处理边界
        nums.insert(0, 1)
        nums.append(1)
        
        dp = [[0]*len(nums) for i in range(len(nums))]

        # 在开区间 i, j 可能获得的最多金币
        def range_best(i, j):
            # k 是最后一个被戳的气球
            m = 0
            for k in range(i+1, j):
                tmp = dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]
                if tmp > m:
                    m = tmp
            dp[i][j] = m

        
        # 遍历每个区间长度 n
        for n in range(3, len(nums)+1):
            # 遍历每个开区间左坐标 i
            for i in range(0, len(nums)-n+1):
                range_best(i, i+n-1)
        
        return dp[0][len(nums)-1]

        
# @lc code=end

