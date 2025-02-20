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
        for i in range(min(len(head), len(tail))):
            if head[i] != tail[i]:
                return lcp
            else:
                lcp += head[i]
        return lcp
        
# @lc code=end

