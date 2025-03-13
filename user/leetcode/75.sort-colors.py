#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i, j 把 0 换到前面
        # j, k 把 2 换到后面
        n = len(nums)
        if n < 2 : return
        
        i = j = 0
        k = n-1
        
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
        
        
# @lc code=end

