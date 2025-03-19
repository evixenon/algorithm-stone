#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def check(node, left, right):
            if not node: return True
            return left < node.val < right and check(node.left, left, node.val) and check(node.right, node.val, right)
        return check(root, -inf, inf)
            
        
# @lc code=end

