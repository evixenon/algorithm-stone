#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        ans.append(intervals[0])
        for l, r in intervals:
            if l <= ans[-1][1]:
                ans[-1][1] = max(r, ans[-1][1])
            else:
                ans.append([l,r])
            
        return ans
# @lc code=end

