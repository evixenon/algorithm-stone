#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n-1
        pre_max = height[0]
        suf_max = height[n-1]
        while left < right: # 最后必然在最高点所以不需要等于
            if pre_max < suf_max:
                ans += min(pre_max, suf_max) - height[left]
                left += 1
                pre_max = max(pre_max, height[left])
            else:
                ans += min(pre_max, suf_max) - height[right]
                right -= 1
                suf_max = max(suf_max, height[right])
                
        return ans
            
# @lc code=end
