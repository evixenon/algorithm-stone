# @before-stub-for-debug-begin
from python3problem114 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flattenNode(node):
            if not node: return None

            # 左尾.next = 右头
            right = node.right
            left = node.left

            left_tail = flattenNode(left)
            if left: # 左子树不为空
                left_tail.right = right
                node.right = left
                node.left = None
                
            right_tail = flattenNode(right)
                
            return right_tail or left_tail or node
        
        flattenNode(root)
        return root
        
# @lc code=end

