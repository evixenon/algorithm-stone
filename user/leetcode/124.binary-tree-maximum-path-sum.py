# @before-stub-for-debug-begin
from python3problem124 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        def dfs(node):
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            # 实时更新经过当前节点的左右子节点的路径
            self.ans = max(self.ans, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax) 

        dfs(root)
        return self.ans
# @lc code=end

