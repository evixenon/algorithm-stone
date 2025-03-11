# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target = target / 2
        
        @cache
        def dfs(i, w):
            if i >= len(nums):
                return False
            elif nums[i] == w:
                return True
            elif nums[i] > w: # 不能选
                return dfs(i+1, w)
            else:
                return dfs(i+1, w) or dfs(i+1, w-nums[i])

        ans = dfs(0, target)
        return ans
        
# @lc code=end

