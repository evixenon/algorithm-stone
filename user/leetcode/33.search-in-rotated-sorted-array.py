# @before-stub-for-debug-begin
from python3problem33 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        - 红色是t左侧, 蓝色是t及右侧
        - 怎么知道 m 前有序还是 m 后有序? 跟最后一个数比. m 更小则后方有序
        """
        # 左闭右开
        l = 0
        r = len(nums)

        last = nums[-1]
        if last == target: return len(nums)-1

        while l < r: # 区间为空 停止
            m = (l + r) // 2
            if nums[m] == target: return m

            if nums[m] > last: # m左侧有序
                if target < nums[m] and target > last: # t在m左
                    r = m
                else:
                    l = m+1
            else: # m 右侧有序
                if target >= nums[m] and target <= last: # t在m及其右
                    l = m+1
                else:
                    r = m
                
        return -1
                

        
        
# @lc code=end

