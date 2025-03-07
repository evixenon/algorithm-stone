#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 背包 容量是取正值的数的和
        # m = (s+target)/2
        m = sum(nums) + target
        if m < 0 or m % 2:
            return 0
        m = m / 2

        # i 是第 i 个物品, c 是剩余容量
        @cache # cache大法避免重复计算
        def dfs(i, c):
            if i < 0: # 没有容量了
                return 1 if c == 0 else 0 # 刚好装满才算一种方案
            if nums[i] > c: # 不够装
                return dfs(i-1, c) # 不选, 遍历下一个物品
            else:
                return dfs(i-1, c) + dfs(i-1, c-nums[i]) # 选和不选的方案数相加
        return dfs(len(nums)-1, m)

        
# @lc code=end

