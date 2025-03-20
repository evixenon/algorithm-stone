#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2: return s

        start = 0
        end = 0
        n = len(s)
        # 用 dp[l][r] 记录 s[l:r+1] 是否回文
        dp = [[0]*n for _ in range(n)]
        for r in range(1, n):
            for l in range(r):
                # r-l <= 2: l和r中间只有0或1个数字
                if (s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1])):
                    dp[l][r] = True
                    if r-l > end-start:
                        start = l
                        end = r
        return s[start:end+1]
# @lc code=end
