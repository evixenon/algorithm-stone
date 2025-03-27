# @before-stub-for-debug-begin
from python3problem621 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 桶理论
        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1
        
        occurs = sorted(d.items(), key=lambda x:x[1], reverse=True)
        max_cnt = occurs[0][1]
        i = 0
        while i < len(occurs) and occurs[i][1] == max_cnt:
            i += 1
        
        return max(len(tasks), (max_cnt-1) * (n+1) + i)
# @lc code=end

