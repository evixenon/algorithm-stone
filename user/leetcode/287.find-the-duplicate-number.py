# @before-stub-for-debug-begin
from python3problem287 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 142 环型链表找回路入口的思想
        fast = 0
        slow = 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast

        
            
# @lc code=end

