#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 遍历回文中心点
        num = 0
        n = len(s)
        for i in range(n):
            # 单数
            num += 1
            l, r = i-1, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                num += 1
                l -= 1
                r += 1

            # 双数
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                num += 1
                l -= 1
                r += 1
        return num

# @lc code=end

