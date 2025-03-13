#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = -1 # 如果找不到
        minv = nums[-1]
        maxv = nums[0]
        n = len(nums)
        for i in range(n):
            # 从左到右维持升序
            if nums[i] < maxv:
                right = i
            else:
                maxv = nums[i]
            # 从右到左维持降序
            if nums[n-i-1] > minv:
                left = n-i-1
            else:
                minv = nums[n-i-1]
        return right - left + 1

        
# @lc code=end

