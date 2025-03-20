#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # # dfs(i) 以坐标i位置结尾的 LIS 长度
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 1
        #     max_prev_length = 0 # 可选i的情况中最长的
        #     for j in range(0, i):
        #         if nums[j] < nums[i]:
        #             max_prev_length = max(max_prev_length, dfs(j))
        #     return max_prev_length + 1
        
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, dfs(i))
        # return ans
        
        f = [0] * n
        f[0] = 1
        ans = 0
        for i in range(n):
            max_prev_length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_prev_length = max(max_prev_length, f[j])
            f[i] = max_prev_length + 1
            ans = max(f[i], ans)
        return ans
# @lc code=end

