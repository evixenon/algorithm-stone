# @before-stub-for-debug-begin
from python3problem215 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, k):
            pivot = nums[0]
            greater = [x for x in nums if x > pivot]
            less = [x for x in nums if x < pivot]
            if len(greater) >= k:
                return quickselect(greater, k)
            elif len(nums) - len(less) < k:
                return quickselect(less, k-len(nums)+len(less))
            return pivot
        return quickselect(nums, k)
        
# @lc code=end

