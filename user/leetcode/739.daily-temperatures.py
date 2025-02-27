# @before-stub-for-debug-begin
from python3problem739 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans
                    
# @lc code=end

