# @before-stub-for-debug-begin
from python3problem238 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp *= nums[i+1] 
            ans[i] *= tmp 
        return ans

        
# @lc code=end
