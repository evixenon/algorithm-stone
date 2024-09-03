# @before-stub-for-debug-begin
from python3problem704 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while (start <= end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
# @lc code=end

