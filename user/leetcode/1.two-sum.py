#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if target-num in d:
                return [i, d[target-num]]
            else:
                d[num] = i
        return 0
        
# @lc code=end

