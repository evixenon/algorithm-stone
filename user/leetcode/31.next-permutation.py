# @before-stub-for-debug-begin
from python3problem31 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右向左查找第一对不是降序的 k, k+1
        n = len(nums)
        if n == 1: return nums
        k = n - 2
        while nums[k] >= nums[k+1]:
            k -= 1
            if k < 0: # 特例
                nums[:] = sorted(nums)
                return

        # 从右向左查找第一个 大于 nums[k] 的数, 交换
        i = n - 1
        while nums[i] <= nums[k]:
            i -= 1
        nums[k], nums[i] = nums[i], nums[k]
        
        # 排列 k + 1 及之后的数列
        nums[k+1:] = sorted(nums[k+1:])
        
        
        
        
# @lc code=end

