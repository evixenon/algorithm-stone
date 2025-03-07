#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        nums = set(nums) # set 的 in 操作会更快
        for num in range(1, n+1):
            if num not in nums:
                ans.append(num)
        return ans
        
# @lc code=end

