# @before-stub-for-debug-begin
from python3problem437 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = {0:1}
        
        def dfs(cur, preSum):
            if not cur: return 0
            preSum += cur.val
            res = count.get(preSum-targetSum, 0)
            count[preSum] = count.get(preSum, 0) + 1
            res += dfs(cur.left, preSum) + dfs(cur.right, preSum)
            count[preSum] -= 1
            return res
        
        return dfs(root, 0)

        
# @lc code=end

