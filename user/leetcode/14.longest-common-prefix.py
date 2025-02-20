#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        head = strs[0]
        tail = strs[-1]
        
        lcp = ""
        for i in range(len(head)):
            if head[i] == tail[i]:
                lcp += head[i]
            else:
                return lcp
        return lcp
        
# @lc code=end

