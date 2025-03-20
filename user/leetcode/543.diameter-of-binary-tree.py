#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 经过某个点且能往上传的最长直径 = 最长左/右 + 1
        # 同时过左右的不能再往上传, 要实时更新ans
        self.ans = 0
        
        def nodes_downwards(node) -> int:
            if not node : return 0
            left = nodes_downwards(node.left)
            right = nodes_downwards(node.right)

            # 实时更新
            self.ans = max(self.ans, left+right)

            return max(left, right) + 1
        
        nodes_downwards(root)
        return self.ans
        
        
# @lc code=end

