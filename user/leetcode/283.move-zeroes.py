#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0 # 指向第一个0, 与i相同时原地换
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            # nums[i] 为 0 时, zero 不动, 而 i 会向后直到非 0 的数
        return nums
            
        
# @lc code=end

