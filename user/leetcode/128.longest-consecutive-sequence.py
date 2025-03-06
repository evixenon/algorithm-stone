#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)
        
        for num in num_set:
            # 如果前序的数命中就不重复计算了
            if not num-1 in num_set:
                streak = 1
                cur = num
                while cur+1 in num_set:
                    cur = cur+1
                    streak += 1
                ans = max(ans, streak)
        return ans
        
# @lc code=end

