#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        # 注意到, 在返回的数组 ans 中, 深度为 i 的节点值记录在 ans[i] 位置
        ans = []
        def levelOrder(node, depth):
            if not node: return

            if len(ans) <= depth:
                ans.append([])
            ans[depth].append(node.val)
            
            levelOrder(node.left, depth+1)
            levelOrder(node.right, depth+1)
        levelOrder(root, 0)
        return ans
            
        
        
# @lc code=end

