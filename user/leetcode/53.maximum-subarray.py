#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        ans = dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if dp[i-1] < 0: # 前面只有负收益
                dp[i] = nums[i] # 重新开始 
            else:
                dp[i] = dp[i-1] + nums[i]
            ans = max(ans, dp[i])
        return ans
        
# @lc code=end

