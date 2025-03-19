#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return
        def isSame(p, q):
            if not p or not q:
                return p is q
            return p.val == q.val and isSame(p.left, q.right) and isSame(p.right, q.left)
        return isSame(root.left, root.right)
        
# @lc code=end

