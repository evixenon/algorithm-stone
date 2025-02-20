#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 设 A 链表不相交长度为 x, B 链表不相交长度为 y, 两链表相交长度为 z
        # 这里最妙的是, x + y + z 总是相等的
        # 因此, 设立双指针, 分别从两条链表头部开始同步走, 到空节点时去到另一条链表开头走
        # 如果 x=y, 那么走完 x/y 步就会来到同一个节点
        # 如果 x!=y, 那么走完 x+z+y/y+z+x 也会到同一节点
        # 又或者不相交, 走完 x+y 就会来到空节点
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
        
# @lc code=end

