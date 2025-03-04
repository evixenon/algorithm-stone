#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        st = []
        while head:
            st.append(head.val)
            head = head.next
        cur = ListNode(st.pop())
        ret = cur
        while st:
            cur.next = ListNode(st.pop())
            cur = cur.next
        return ret
        
# @lc code=end

