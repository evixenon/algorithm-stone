#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # 返回两个参数减少重复函数执行
        def dfs(node):
            if not node:
                return 0, 0
            
            left_rob, left_norob = dfs(node.left)
            right_rob, right_norob = dfs(node.right)
            
            # 劫此节点, 子节点不能劫
            rob = left_norob + right_norob + node.val

            # 不劫子节点
            norob = max(left_norob, left_rob) + max(right_norob, right_rob)
            return rob, norob
            
        return max(dfs(root))
# @lc code=end

