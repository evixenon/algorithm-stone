# @before-stub-for-debug-begin
from python3problem560 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 记录前缀和出现次数
        count = {0:1}  # 默认初始化
        preSum = 0
        res = 0
        for num in nums:
            preSum += num
            targetNum = count.get(preSum-k, 0)
            res += targetNum
            count[preSum] = count.get(preSum, 0) + 1
        return res
        
# @lc code=end

