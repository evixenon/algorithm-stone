# @before-stub-for-debug-begin
from python3problem394 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        cur = ""
        multi = 0
        for c in s:
            if c == '[':
                st.append((multi, cur))
                cur = ""
                multi = 0
            elif c == ']':
                n, last = st.pop(-1)
                cur = last + cur * n
            elif c.isdigit():
                multi = multi * 10 + int(c)
            else:
                cur += c
        ans = cur
        return ans
                
        
# @lc code=end

