#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        fast = slow = head
        while True:
            if not (fast and fast.next): return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                break
        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None
        

        
# @lc code=end

