# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution: 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        left = 0
        cur = 0 # [left, right]的值
        for right, x in enumerate(nums):
            cur += x
            while cur >= target:
                ans = min(ans, right-left+1)
                cur -= nums[left]
                left += 1
        return ans if ans <= n else 0
            
        
# @lc code=end

