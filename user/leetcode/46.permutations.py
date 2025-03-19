#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        ans = []
        def dfs(selected, rest):
            if not rest:
                ans.append(selected)
                return
            for i in nums:
                if i in selected:
                    continue
                dfs(selected+[i], rest-1)
        dfs([], n)
        return ans
# @lc code=end

