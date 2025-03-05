# @before-stub-for-debug-begin
from python3problem148 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        # 截断点
        if not head.next: return head
        
        # 快慢指针找到奇数中点, 偶数中点左
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # cut, mid 是中点右边
        mid = slow.next
        slow.next = None
        
        # 进行递归排序
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # merge
        res = tmp = ListNode(0)
        while left and right:
            if left.val < right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        tmp.next = left if left else right
        return res.next
# @lc code=end

