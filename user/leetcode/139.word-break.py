# @before-stub-for-debug-begin
from python3problem139 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(dp)):
            for j in range(i+1, len(dp)):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
                
        
# @lc code=end

