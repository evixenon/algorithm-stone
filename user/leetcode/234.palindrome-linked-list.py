# @before-stub-for-debug-begin
from python3problem234 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        fast = head
        slow = head
        while fast and fast.next:
            st.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != st.pop():
                return False
            slow = slow.next
        return True
        
# @lc code=end

