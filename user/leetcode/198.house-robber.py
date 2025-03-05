# @before-stub-for-debug-begin
from python3problem198 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        maxMoney = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            maxMoney = max(dp[i], maxMoney)
        return maxMoney
        
# @lc code=end

