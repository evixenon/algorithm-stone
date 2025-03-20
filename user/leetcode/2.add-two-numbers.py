# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        dummy = cur = ListNode()
        while l1 and l2:
            s = l1.val + l2.val + c
            c = s // 10
            cur.next = ListNode(val=s%10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 or l2 or c:
            if l1:
                s = l1.val + c
                l1 = l1.next
            elif l2:
                s = l2.val + c
                l2 = l2.next
            else:
                s = c
            c = s // 10
            cur.next = ListNode(val=s%10)
            cur = cur.next

        return dummy.next
        
# @lc code=end

