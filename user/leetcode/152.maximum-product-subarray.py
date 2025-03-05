# @before-stub-for-debug-begin
from python3problem152 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = prev_max = prev_min = nums[0]
        for i in range(1, len(nums)):
            maxp = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            minp = min(prev_max * nums[i], prev_min * nums[i], nums[i])
            dp = max(dp, maxp)
            prev_max = maxp
            prev_min = minp
        return dp
        
        
# @lc code=end

