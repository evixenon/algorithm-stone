#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        # 如果能跳到 i, 那 i 以前的位置都能跳
        for i, step in enumerate(nums):
            if i <= max_pos:
                max_pos = max(max_pos, i+step)
        return max_pos >= len(nums)-1
# @lc code=end

