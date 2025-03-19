#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 对于每个元素, 都有选和不选两种可能的操作
        n = len(nums)
        def dfs(selected, i):
            if i == n:
                ans.append(selected)
                return
            dfs(selected, i+1)
            dfs(selected+[nums[i]], i+1)
        dfs([], 0)
        return ans
        
# @lc code=end

