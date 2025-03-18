# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(t):
            # 左闭右开
            l = 0
            r = len(nums)
            while l<r:
                m = l + (r-l)//2
                if nums[m] < t:
                    l = m + 1
                else:
                    r = m
            return l

        # 大于等于目标的 lower_bound
        start = lower_bound(target)
        if start > len(nums)-1 or nums[start] != target: return [-1, -1]
        # 结束点 = 目标+1 lower_bound 的前一个位置
        end = lower_bound(target+1) -1
        return [start, end]
        
# @lc code=end

