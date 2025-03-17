# @before-stub-for-debug-begin
from python3problem713 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        ans = 0
        left = 0
        prod = 1
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right-left+1
        return ans
        
# @lc code=end

