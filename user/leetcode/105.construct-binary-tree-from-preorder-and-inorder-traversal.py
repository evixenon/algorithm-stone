# @before-stub-for-debug-begin
from python3problem105 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 重点在分割左子树和右子树
        def build(preorder, inorder):
            if not inorder:
                return None
            v = preorder[0]
            
            # 将 inorder 以 v 为界分开, 左边是左子树, 右边是右子树
            # left_len = 0
            # while inorder[left_len] != v:
            #     left_len += 1
            left_len = dic[v] - dic[inorder[0]]
            
            next_left_inorder = inorder[:left_len]
            next_right_inorder = inorder[left_len+1:]

            next_left_preorder = preorder[1:1+left_len]
            next_right_preorder = preorder[1+left_len:]

            left = build(next_left_preorder, next_left_inorder)
            right = build(next_right_preorder, next_right_inorder)

            node = TreeNode(val=v, left=left, right=right)
            
            return node
        
        # 加个哈希加速
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        
        return build(preorder, inorder)
        
# @lc code=end

